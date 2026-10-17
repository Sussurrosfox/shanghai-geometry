import asyncio
import os
import re
import httpx
from openai import AsyncOpenAI

# ================= 配置区域 =================
# 请在此处填入你的 API 配置
API_KEY = "sk-geminixxxxx"      # 你的 API Key
BASE_URL = "http://127.0.0.1:18765/v1/"  # API 地址 (如果是中转或非官方，请修改此处)
MODEL_NAME = "gemini-3-pro"                 # 使用的模型名称
INTERVAL_SECONDS = 1                  # 发送间隔 (秒)
# ===========================================

# 所有输入/输出文件均以脚本所在目录为基准，避免受当前工作目录影响
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 初始化异步客户端（禁用系统代理，避免本地 API 被错误转发）
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL.strip(),  # 移除可能的多余空格
    http_client=httpx.AsyncClient(trust_env=False)
)

def find_image_in_markdown(content: str, base_dir: str = SCRIPT_DIR) -> str | None:
    """
    从 Markdown 内容中解析第一个图片引用，如 ![alt](images/xxx.jpg)
    相对路径基于 base_dir（默认脚本所在目录）解析
    返回解析到且实际存在的图片路径，否则返回 None
    """
    match = re.search(r'!\[.*?\]\((.*?)\)', content)
    if not match:
        return None
    image_path = match.group(1).strip()
    if not os.path.isabs(image_path):
        image_path = os.path.join(base_dir, image_path)
    if os.path.exists(image_path):
        return image_path
    print(f"[警告] Markdown 中引用的图片 {image_path} 不存在，将不发送图片。")
    return None

async def solve_problem(k: int):
    """
    读取 k.md，调用 API，并将结果写入 k_solution.md
    支持发送 Markdown 中引用的图片文件
    优化：如果解决方案文件已存在，则跳过处理
    所有文件均以脚本所在目录为基准，不受当前工作目录影响
    """
    input_filename = f"{k}.md"
    output_filename = f"{k}_solution.md"
    input_path = os.path.join(SCRIPT_DIR, input_filename)
    output_path = os.path.join(SCRIPT_DIR, output_filename)

    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        print(f"[跳过] 文件 {input_filename} 不存在。")
        return

    # === 检查：跳过已存在的解决方案文件 ===
    if os.path.exists(output_path):
        if os.path.getsize(output_path) > 0:
            print(f"[跳过] 解决方案 {output_filename} 已存在，跳过处理。")
            return
        # 空文件说明上次写入未完成，不能当作已处理
        print(f"[信息] 解决方案 {output_filename} 为空文件（上次写入未完成），将重新生成。")
    # ======================================

    try:
        # 1. 读取题目
        with open(input_path, 'r', encoding='utf-8') as f:
            question_content = f.read()

        # 2. 从 Markdown 内容中解析图片路径
        image_path = find_image_in_markdown(question_content)
        
        print(f"[开始处理] 题目 {input_filename}..." + (f" (含图片 {image_path})" if image_path else ""))

        # 3. 构建请求：有图片时通过 files 字段发送图片绝对路径
        extra_body = {}
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
        # 先写临时文件再原子替换，避免写入中断留下残缺文件被误判为已完成
        tmp_path = output_path + ".tmp"
        with open(tmp_path, 'w', encoding='utf-8') as f:
            # 写入题干部分
            f.write(f"## 题目 ({k}.md)\n\n")
            f.write(question_content)
            f.write("\n\n---\n\n")

            # 写入解答部分，并包裹在 solution 环境中
            f.write("\\begin{solution}\n\n")
            f.write(answer_content)
            f.write("\n\n\\end{solution}")
        os.replace(tmp_path, output_path)

        print(f"[完成] 已生成 {output_filename}")

    except Exception as e:
        print(f"[错误] 处理 {input_filename} 时出错: {e}")

async def main_scheduler(total_files: int):
    """
    调度器：串行处理每个题目，一次只处理一题
    """
    print(f"开始串行处理 {total_files} 个文件，每题处理完成后再处理下一题...")

    for k in range(1, total_files + 1):
        # 串行处理：等待当前任务完成后再处理下一个
        await solve_problem(k)

        # 如果不是最后一个文件，暂停指定时间
        if k < total_files:
            await asyncio.sleep(INTERVAL_SECONDS)

    print("全部处理完成！")
    await client.close()

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