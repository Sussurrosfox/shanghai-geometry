import asyncio
import os
import re
import httpx
from openai import AsyncOpenAI

# ================= 配置区域 =================
# 请在此处填入你的 API 配置
API_KEY = "sk-geminixxxxx"      # 你的 API Key
BASE_URL = "http://127.0.0.1:18767/v1/"  # API 地址；多账号模式下默认轮询所有账号，也可改为 ".../a/c1/v1/" 固定使用容器 1 的账号
MODEL_NAME = "gemini-4-argon"             # 使用的模型名称
REASONING_EFFORT = "high"               # 思考强度: low / medium / high (映射到扩展思考)
INTERVAL_SECONDS = 1                  # 发送间隔 (秒)
QUOTA_RETRY_SECONDS = 60              # 额度耗尽后的重新查询间隔 (秒)
QUOTA_REQUEST_TIMEOUT = 30            # 额度查询超时时间 (秒)
# ===========================================

QUOTA_URL = f"{BASE_URL.strip().rstrip('/')}/quota"

# 初始化异步客户端（禁用系统代理，避免本地 API 被错误转发）
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL.strip(),  # 移除可能的多余空格
    http_client=httpx.AsyncClient(trust_env=False)
)
quota_client = httpx.AsyncClient(
    trust_env=False,
    timeout=QUOTA_REQUEST_TIMEOUT,
)

def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def find_exhausted_quotas(payload: dict, model_name: str = MODEL_NAME) -> list[dict]:
    """返回当前模型及账户级用量窗口中已经耗尽的额度。"""
    if not isinstance(payload, dict):
        return []

    quotas = payload.get("quotas", {})
    if not isinstance(quotas, dict):
        return []

    exhausted = []
    relevant_action_ids = {11, 15} if "flash" in model_name.lower() else {4, 6, 15}
    for quota_id, quota in quotas.items():
        if quota_id in {"extra", "usage_info"} or not isinstance(quota, dict):
            continue
        if quota.get("action_id") not in relevant_action_ids:
            continue

        remaining = quota.get("remaining")
        total = quota.get("total")
        usage_percentage = quota.get("usage_percentage")
        is_unlimited = remaining == 0 and total == 0
        is_exhausted = not is_unlimited and (
            (_is_number(remaining) and remaining <= 0)
            or (_is_number(usage_percentage) and usage_percentage >= 100)
        )
        if is_exhausted:
            exhausted.append({"quota_id": quota_id, **quota})

    usage_info = payload.get("usage_info") or quotas.get("usage_info") or {}
    if isinstance(usage_info, dict):
        for key in ("current_5h", "weekly"):
            metric = usage_info.get(key)
            if not isinstance(metric, dict):
                continue
            remaining = metric.get("remaining_credits")
            usage_percentage = metric.get("usage_percentage")
            if (
                _is_number(remaining) and remaining <= 0
            ) or (
                _is_number(usage_percentage) and usage_percentage >= 100
            ):
                exhausted.append({"quota_id": f"usage_info.{key}", **metric})

    return exhausted


def _format_quota(quota: dict) -> str:
    label = quota.get("label") or quota.get("window") or quota["quota_id"]
    remaining = quota.get("remaining", quota.get("remaining_credits", "?"))
    total = quota.get("total")
    amount = f"{remaining}/{total}" if total is not None else str(remaining)
    reset = quota.get("reset_at") or quota.get("reset_time")
    reset_text = f"，重置时间: {reset}" if reset else ""
    return f"{label}（剩余: {amount}{reset_text}）"


def quota_alarm(message: str) -> None:
    """输出终端报警，并在 Windows 上尝试播放系统提示音。"""
    print(f"\a[额度报警] {message}", flush=True)
    if os.name == "nt":
        try:
            import winsound

            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        except (ImportError, RuntimeError):
            pass


async def fetch_quota() -> dict:
    response = await quota_client.get(
        QUOTA_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    response.raise_for_status()
    return response.json()


def check_quota_payload(payload: dict, model_name: str = MODEL_NAME) -> tuple[bool, str]:
    """
    检查额度负载，兼容单账号与多账号两种返回格式：
    - 单账号: {"quotas": ..., "usage_info": ...}
    - 多账号聚合: {"accounts": {"c1": {"quotas": ...}, ...}}
    返回 (是否有可用额度, 详情描述)。多账号模式下只要还有一个账号可用即视为可用。
    """
    if not isinstance(payload, dict):
        return True, "额度接口返回格式无法识别"

    accounts = payload.get("accounts")
    if isinstance(accounts, dict) and accounts:
        available, exhausted_details, error_names = [], [], []
        for name, acc in accounts.items():
            if not isinstance(acc, dict) or "error" in acc or not isinstance(acc.get("quotas"), dict):
                error_names.append(name)
                continue
            exhausted = find_exhausted_quotas(acc, model_name)
            if exhausted:
                exhausted_details.append(
                    f"[{name}] " + "；".join(_format_quota(q) for q in exhausted)
                )
            else:
                available.append(name)
        if available:
            return True, f"可用账号: {', '.join(available)}"
        if error_names and not exhausted_details:
            # 所有账号都无法评估时不阻塞主流程
            return True, f"以下账号额度查询失败: {', '.join(error_names)}"
        details = "；".join(exhausted_details)
        if error_names:
            details += f"；以下账号查询失败: {', '.join(error_names)}"
        return False, details or "所有账号额度均不可用"

    if isinstance(payload.get("quotas"), dict):
        exhausted = find_exhausted_quotas(payload, model_name)
        if not exhausted:
            return True, ""
        return False, "；".join(_format_quota(q) for q in exhausted)

    return True, "额度接口返回格式无法识别"


async def wait_for_quota_available() -> None:
    """额度耗尽时暂停当前调度，定期查询直至恢复。多账号模式下仅当所有账号均耗尽时才暂停。"""
    paused = False
    while True:
        try:
            payload = await fetch_quota()
            available, details = check_quota_payload(payload)
            if available:
                if paused:
                    print(f"[信息] 额度已恢复{(f'（{details}）') if details else ''}，继续处理当前题目。")
                elif details:
                    print(f"[警告] {details}，将继续原处理流程。")
                return

            paused = True
            quota_alarm(
                f"{MODEL_NAME} 相关额度已耗尽：{details}。"
                f"已暂停，{QUOTA_RETRY_SECONDS} 秒后重新查询。"
            )
        except Exception as e:
            if not paused:
                print(f"[警告] 额度查询失败: {e}，将继续原处理流程。")
                return
            print(f"[警告] 暂停期间额度查询失败: {e}，稍后重试。")

        await asyncio.sleep(QUOTA_RETRY_SECONDS)


def find_image_in_markdown(content: str) -> str | None:
    """
    从 Markdown 内容中解析第一个图片引用，如 ![alt](images/xxx.jpg)
    返回解析到且实际存在的图片路径，否则返回 None
    """
    match = re.search(r'!\[.*?\]\((.*?)\)', content)
    if not match:
        return None
    image_path = match.group(1).strip()
    if os.path.exists(image_path):
        return image_path
    print(f"[警告] Markdown 中引用的图片 {image_path} 不存在，将不发送图片。")
    return None

def is_solution_complete(path: str) -> bool:
    """
    判断解答文件是否完整。
    完整的解答文件由本脚本完整写入，以 \\end{solution} 结尾；
    空文件或中途异常留下的残缺文件视为未处理，需要重新生成。
    """
    try:
        if os.path.getsize(path) == 0:
            return False
        with open(path, "r", encoding="utf-8") as f:
            return "\\end{solution}" in f.read()
    except OSError:
        return False


async def solve_problem(k: int):
    """
    读取 k.md，调用 API，并将结果写入 k_solution.md
    支持发送 Markdown 中引用的图片文件
    优化：如果解决方案文件已存在，则跳过处理
    """
    input_filename = f"{k}.md"
    output_filename = f"{k}_solution.md"

    # === 检查：跳过已存在且完整的解决方案文件 ===
    if os.path.exists(output_filename):
        if is_solution_complete(output_filename):
            print(f"[跳过] 解决方案 {output_filename} 已存在且完整，跳过处理。")
            return
        print(f"[警告] {output_filename} 存在但不完整（可能由上次中断/失败产生），将重新生成。")
    # ======================================

    # 检查输入文件是否存在
    if not os.path.exists(input_filename):
        print(f"[跳过] 文件 {input_filename} 不存在。")
        return

    # 在真正生成前确认当前模型及账户级额度仍然可用。
    await wait_for_quota_available()

    try:
        # 1. 读取题目
        with open(input_filename, 'r', encoding='utf-8') as f:
            question_content = f.read()

        # 2. 从 Markdown 内容中解析图片路径
        image_path = find_image_in_markdown(question_content)
        
        print(f"[开始处理] 题目 {input_filename}..." + (f" (含图片 {image_path})" if image_path else ""))

        # 3. 构建请求：附加思考强度；有图片时通过 files 字段发送图片绝对路径
        extra_body = {"reasoning_effort": REASONING_EFFORT}
        if image_path:
            extra_body["files"] = [os.path.abspath(image_path)]

        # 4. 调用 API
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": question_content}
            ],
            temperature=0.3,
            extra_body=extra_body
        )

        answer_content = response.choices[0].message.content
        if not answer_content:
            raise ValueError("API 返回内容为空，未生成解答")

        # 打印实际使用的模型
        print(f"[信息] 实际使用的模型: {response.model}")
        if hasattr(response, 'actual_model_used') and response.actual_model_used:
            print(f"[信息] 实际模型详情: {response.actual_model_used}")

        # 检查实际使用的模型是否包含 "flash" 字样，如果是则终止程序
        if "flash" in response.model.lower():
            print("检测到实际使用的是 Flash 模型，程序终止")
            exit(1)
            
        if hasattr(response, 'actual_model_used') and "flash" in response.actual_model_used.lower():
            print("检测到实际使用的是 Flash 模型，程序终止")
            exit(1)

        # 检查返回内容是否包含"无法解析响应"
        if "无法解析响应" in answer_content:
            print("Cookie 已失效请更新")
            exit(1)

        # 5. 写入文件 (题目 + 答案)
        # 先写临时文件再原子替换，避免中断/异常留下残缺文件被误认为已处理
        tmp_filename = output_filename + ".tmp"
        with open(tmp_filename, 'w', encoding='utf-8') as f:
            # 写入题干部分
            f.write(f"## 题目 ({k}.md)\n\n")
            f.write(question_content)
            f.write("\n\n---\n\n")

            # 写入解答部分，并包裹在 solution 环境中
            f.write("\\begin{solution}\n\n")
            f.write(answer_content)
            f.write("\n\n\\end{solution}")
        os.replace(tmp_filename, output_filename)

        print(f"[完成] 已生成 {output_filename}")

    except Exception as e:
        print(f"[错误] 处理 {input_filename} 时出错: {e}")

async def main_scheduler(total_files: int):
    """
    调度器：串行处理每个题目，一次只处理一题
    """
    print(f"开始串行处理 {total_files} 个文件，每题处理完成后再处理下一题...")

    try:
        for k in range(1, total_files + 1):
            # 串行处理：等待当前任务完成后再处理下一个
            await solve_problem(k)

            # 如果不是最后一个文件，暂停指定时间
            if k < total_files:
                await asyncio.sleep(INTERVAL_SECONDS)

        print("全部处理完成！")
    finally:
        await client.close()
        await quota_client.aclose()

if __name__ == "__main__":
    # 询问用户要处理的文件数量
    try:
        user_input = input("请输入要处理的文件数量 N: ").strip()
        total_files = int(user_input)
        if total_files <= 0:
            raise ValueError("文件数量必须为正整数")
    except ValueError as e:
        print(f"输入无效: {e}")
        exit(1)

    # 运行主程序
    asyncio.run(main_scheduler(total_files))