import asyncio
import os
import aiohttp
import json
import traceback
import csv
import random
import shutil
from collections import deque
from dataclasses import dataclass, field
from typing import List
import re

# ================= 配置区域 =================

# Intern API 访问地址（不带 /api/v1）
BASE_URL = "https://chat.intern-ai.org.cn/api"

# Intern API 配置（已硬编码，原从 apis.csv 读取）
INTERN_API_KEY = "sk-2jrOWHaphuL1C8Qk8GFE2DgQfxXMD7DvScnkMoLd01V5dWaf"

# 模型名称
INTERN_MODEL_NAME = "intern-s2-preview"
MODEL_NAME = INTERN_MODEL_NAME.split("（")[0].strip()
# 总保持 thinking 关闭
DISABLE_THINKING = True

MAX_CONCURRENT = 5         # 并发上限（Intern AI 单 key rpm <= 50，保守设为 5）
MAX_RETRIES = 5            # 最大重试次数
FAILURE_FILE = "failure_translator.csv"  # 失败记录文件
API_INTERVAL = 1.5         # 每两次 API 调用之间的间隔（秒）

# Prompt 文件路径
PROMPT_FILE = "PARAPHRASE_PROMPT.txt"

# 备份文件夹
BACKUP_DIR = "backup"

# ===========================================

def load_prompt(filename: str) -> str:
    """
    从文件中读取 prompt 内容。
    """
    if not os.path.exists(filename):
        print(f"[错误] 未找到 prompt 文件: {filename}")
        exit(1)
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"[信息] 成功从 {filename} 加载 prompt。")
    return content


# 加载 prompt
prompt = load_prompt(PROMPT_FILE)

# 预加载 API Key（使用上方硬编码的单 Key，不再读取 apis.csv）
API_KEYS_LIST = [INTERN_API_KEY]

# ===========================================

@dataclass
class TaskItem:
    """任务项：记录文件编号 k、重试次数、已使用的 API Key 索引"""
    file_index: int  # 文件编号 k
    retry_count: int = 0
    used_key_indices: List[int] = field(default_factory=list)


def get_next_api_key_index(api_keys: list, used_indices: List[int]) -> int:
    """
    获取下一个未使用的 API Key 索引。
    如果所有 Key 都已使用过，则重置并随机选择一个。
    """
    available_indices = [i for i in range(len(api_keys)) if i not in used_indices]
    if not available_indices:
        # 所有 Key 都试过了，重置并随机选择
        return random.randint(0, len(api_keys) - 1)
    return random.choice(available_indices)


def clean_r1_output(text: str) -> str:
    """
    DeepSeek-R1 模型输出通常包含 <think...>...</think > 思考链标签。
    此函数用于去除思考过程，仅保留最终翻译结果。
    """
    # 优先查找 R1 常见的结束标签 </think >
    if "</think >" in text:
        return text.split("</think >")[-1].strip()

    # 正则兜底：去除所有 <think...>...</think > 内容
    cleaned = re.sub(r"<think.*?>.*?</think\s*>", "", text, flags=re.DOTALL | re.IGNORECASE)
    return cleaned.strip()


def extract_solution_content(file_content: str) -> tuple:
    """
    从文件内容中提取 \\begin{solution} 与 \\end{solution} 之间的内容。
    返回 (before, solution_content, after) 三元组。
    如果未找到，返回 (file_content, None, None)。
    """
    # 使用正则匹配 \\begin{solution} 和 \\end{solution} 之间的内容
    pattern = r'(.*?)(\\begin\{solution\})(.*?)(\\end\{solution\})(.*)'
    match = re.match(pattern, file_content, re.DOTALL)
    
    if match:
        before = match.group(1) + match.group(2)  # 包含 \\begin{solution}
        solution_content = match.group(3)  # 中间内容（不含标记）
        after = match.group(4) + match.group(5)  # 包含 \\end{solution}
        return (before, solution_content, after)
    
    return (file_content, None, None)


async def record_failure(file_index: int, reason: str, lock: asyncio.Lock):
    """
    将失败的文件编号写入 failure_translator.csv
    使用锁确保并发安全。
    """
    async with lock:
        file_exists = os.path.exists(FAILURE_FILE)
        with open(FAILURE_FILE, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["file_index", "reason"])
            writer.writerow([file_index, reason])
        print(f"[记录失败] 文件 {file_index}_solution.md 已写入 {FAILURE_FILE}，原因: {reason}")


async def process_file(
    session: aiohttp.ClientSession,
    task: TaskItem,
    api_keys: list,
    semaphore: asyncio.Semaphore,
    interval_lock: asyncio.Lock,
    last_call_time: list  # 使用 list 作为可变引用
):
    """
    处理单个文件：
    1. 读取 k_solution.md
    2. 备份文件
    3. 提取 \\begin{solution} 与 \\end{solution} 之间的内容
    4. 调用 API 处理
    5. 用处理后内容替换原内容
    失败时返回 False，由调用者决定是否重试。
    """
    file_index = task.file_index
    filename = f"{file_index}_solution.md"
    filepath = filename  # 当前文件夹

    # 用于暂存 API 返回的内容，以便在写入失败时打印
    answer_content = None

    # --- 等待获取信号量（并发控制）---
    async with semaphore:
        # --- 选择一个未使用的 API Key ---
        key_index = get_next_api_key_index(api_keys, task.used_key_indices)
        current_key = api_keys[key_index]
        task.used_key_indices.append(key_index)

        # 打印日志时隐藏 Key 的中间部分，仅显示前后几位以便调试
        masked_key = f"{current_key[:6]}...{current_key[-4:]}"

        try:
            # 1. 读取文件内容
            if not os.path.exists(filepath):
                print(f"[跳过] 文件 {filename} 不存在。")
                return True  # 视为成功（无需处理）

            with open(filepath, "r", encoding="utf-8") as f:
                file_content = f.read()

            retry_info = f"(重试 {task.retry_count}/{MAX_RETRIES})" if task.retry_count > 0 else ""
            print(f"[开始处理] 文件 {filename} {retry_info} (使用 Key: {masked_key})...")

            # 2. 提取 solution 内容
            before, solution_content, after = extract_solution_content(file_content)
            
            if solution_content is None:
                print(f"[跳过] 文件 {filename} 未找到 \\begin{{solution}}...\\end{{solution}} 标记。")
                return True  # 视为成功（无需处理）

            print(f"    提取到 solution 内容: {len(solution_content)} 字符")

            # 3. 构造请求
            url = f"{BASE_URL.rstrip('/')}/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {current_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": MODEL_NAME,
                "messages": [
                    {
                        "role": "system",
                        "content": prompt,
                    },
                    {"role": "user", "content": solution_content},
                ],
                "temperature": 0.3,
                "max_tokens": 8192,
                "thinking_mode": False,  # 总保持 thinking 关闭
            }

            # 4. 调用 Intern API（带间隔控制）
            try:
                # --- 间隔控制：确保两次 API 调用之间间隔 API_INTERVAL 秒 ---
                async with interval_lock:
                    now = asyncio.get_event_loop().time()
                    elapsed = now - last_call_time[0]
                    if elapsed < API_INTERVAL:
                        wait_time = API_INTERVAL - elapsed
                        await asyncio.sleep(wait_time)
                    last_call_time[0] = asyncio.get_event_loop().time()
                # ----------------------------------------------
                async with session.post(url, headers=headers, json=payload, timeout=600) as resp:
                    # 4.1 检查 HTTP 状态码
                    if resp.status != 200:
                        error_text = await resp.text()
                        print(f"\n[!!! 错误 !!!] 文件 {filename} 请求失败 (Key: {masked_key})")
                        print(f"HTTP 状态码: {resp.status}")
                        print(f"服务器响应: {error_text}")
                        return False  # 失败，需要重试

                    # 4.2 尝试解析 JSON
                    try:
                        data = await resp.json()
                    except json.JSONDecodeError as e:
                        raw_text = await resp.text()
                        print(f"\n[!!! 错误 !!!] 文件 {filename} 响应解析失败 (不是有效的 JSON)")
                        print(f"JSON 解析异常: {e}")
                        print(f"原始响应内容: \n{raw_text}")
                        return False  # 失败，需要重试

                    # 4.3 提取内容
                    try:
                        raw_content = data["choices"][0]["message"]["content"]
                        answer_content = clean_r1_output(raw_content)
                    except (KeyError, IndexError) as e:
                        print(f"\n[!!! 错误 !!!] 文件 {filename} 返回的数据格式不符合预期")
                        print(f"数据结构异常: {e}")
                        print(f"完整返回数据: {json.dumps(data, indent=2, ensure_ascii=False)}")
                        return False  # 失败，需要重试

            except aiohttp.ClientError as e:
                print(f"\n[!!! 网络错误 !!!] 文件 {filename} 连接 Open WebUI 失败")
                print(f"异常详情: {e}")
                traceback.print_exc()
                return False  # 失败，需要重试
            except asyncio.TimeoutError:
                print(f"\n[!!! 超时 !!!] 文件 {filename} 请求超时 (600秒)")
                return False  # 失败，需要重试

            # 5. 备份原文件
            try:
                os.makedirs(BACKUP_DIR, exist_ok=True)
                backup_path = os.path.join(BACKUP_DIR, filename)
                shutil.copy2(filepath, backup_path)
                print(f"    已备份到 {backup_path}")
            except IOError as e:
                print(f"\n[!!! 备份失败 !!!] 文件 {filename} 备份失败: {e}")
                return False  # 失败，需要重试

            # 6. 写入文件（用处理后内容替换原 solution 内容）
            try:
                # 重新组装文件内容：before + answer_content + after
                # before 已包含 \\begin{solution}，after 已包含 \\end{solution}
                new_content = before + answer_content + after
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

                print(f"[完成] 已更新 {filename}")
                return True  # 成功

            except IOError as e:
                print(f"\n[!!! 文件写入错误 !!!] 文件 {filename} 写入失败")
                print(f"IO 异常: {e}")
                print(f"\n[=== 以下是已生成的解答内容 (请手动保存) ===]")
                print(answer_content)
                print(f"[=========================================]\n")
                return False  # 失败，需要重试

        except Exception as e:
            # 捕获其他所有未预料到的异常
            print(f"\n[!!! 未知异常 !!!] 处理文件 {filename} 时发生未知错误")
            traceback.print_exc()
            if answer_content:
                print("\n[=== 缓存的解答内容 ===]")
                print(answer_content)
            return False  # 失败，需要重试


async def main_scheduler(file_indices: list, api_keys: list):
    """
    调度器：并发控制，最多同时运行 MAX_CONCURRENT 个任务
    失败时将任务放回队列尾部，更换 API Key 重试，最多 MAX_RETRIES 次
    """
    print(f"开始处理 {len(file_indices)} 个文件，并发上限: {MAX_CONCURRENT}...")
    print(f"API Key 池大小: {len(api_keys)}")
    print(f"最大重试次数: {MAX_RETRIES}")

    # 创建信号量，控制并发数
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    # 创建任务队列
    task_queue = deque()
    for file_index in file_indices:
        task_queue.append(TaskItem(file_index=file_index))

    # 创建锁（用于队列操作和失败记录写入）
    queue_lock = asyncio.Lock()
    failure_lock = asyncio.Lock()
    interval_lock = asyncio.Lock()  # 用于 API 调用间隔控制
    last_call_time = [0.0]  # 使用 list 作为可变引用，记录上次 API 调用时间

    # 统计计数器
    success_count = 0
    failure_count = 0
    stats_lock = asyncio.Lock()

    async with aiohttp.ClientSession() as session:
        async def process_task(task: TaskItem):
            """处理单个任务，失败时重新入队或记录失败"""
            nonlocal success_count, failure_count

            success = await process_file(
                session, task, api_keys, semaphore, interval_lock, last_call_time
            )

            if success:
                async with stats_lock:
                    success_count += 1
            else:
                # 失败，检查是否还能重试
                task.retry_count += 1
                if task.retry_count < MAX_RETRIES:
                    # 放回队列尾部
                    async with queue_lock:
                        task_queue.append(task)
                    print(f"[重试入队] 文件 {task.file_index}_solution.md 将重新处理 (第 {task.retry_count} 次重试)")
                else:
                    # 超过最大重试次数，记录失败
                    await record_failure(task.file_index, f"重试{MAX_RETRIES}次后失败", failure_lock)
                    async with stats_lock:
                        failure_count += 1

        # 持续处理队列中的任务
        active_tasks = set()
        while task_queue or active_tasks:
            # 从队列取出任务
            while task_queue and len(active_tasks) < MAX_CONCURRENT:
                async with queue_lock:
                    if task_queue:
                        task = task_queue.popleft()
                        t = asyncio.create_task(process_task(task))
                        active_tasks.add(t)
                        t.add_done_callback(active_tasks.discard)

            # 等待任意一个任务完成
            if active_tasks:
                await asyncio.wait(
                    active_tasks,
                    return_when=asyncio.FIRST_COMPLETED
                )

    print(f"\n{'='*50}")
    print(f"全部处理完成！")
    print(f"成功: {success_count} 个")
    print(f"失败: {failure_count} 个 (已记录到 {FAILURE_FILE})")
    print(f"{'='*50}")


def batch_process():
    """
    主流程：
    1. 询问用户要处理的文件数 N
    2. 对于每个 1<=k<=N，处理 k_solution.md
    """
    # 交互式询问文件数 N
    try:
        user_input = input("请输入要处理的文件数 N: ").strip()
        N = int(user_input)
        if N < 1:
            print("错误：N 必须是正整数。")
            return
    except ValueError:
        print("错误：请输入有效的正整数。")
        return

    # 生成文件编号列表
    file_indices = list(range(1, N + 1))
    
    print(f"\n将处理以下文件:")
    for k in file_indices:
        filename = f"{k}_solution.md"
        exists = "✓" if os.path.exists(filename) else "✗"
        print(f"  {filename} [{exists}]")
    print()

    # 确认
    confirm = input("确认开始处理？(y/n): ").strip().lower()
    if confirm != 'y':
        print("已取消。")
        return

    # 确保备份文件夹存在
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # 运行异步调度器
    asyncio.run(main_scheduler(file_indices, API_KEYS_LIST))


if __name__ == "__main__":
    batch_process()