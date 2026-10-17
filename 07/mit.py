import os
import re

# ==========================================
# 第一部分：来自 mergeitO.py (合并文件逻辑)
# ==========================================

def merge_files():
    print("\n--- 阶段 1: 合并文件 ---")
    
    # 交互式询问要处理的文件数
    while True:
        try:
            user_input = input("请输入要处理的文件总数: ")
            max_k = int(user_input)
            if max_k <= 0:
                print("请输入大于 0 的整数。")
                continue
            break
        except ValueError:
            print("输入无效，请输入一个整数。")

    # 固定输出文件名 (作为中间文件)
    output_filename = "merged.md"
    processed_contents = []

    print(f"正在查找并合并 1 到 {max_k} 的文件...")

    for k in range(1, max_k + 1):
        # 构建文件名
        filename = f"{k}_solution.md"
        
        # 检查文件是否存在
        if not os.path.exists(filename):
            print(f"警告: 未找到文件 {filename}，已跳过。")
            continue
        
        try:
            # 读取文件
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 1. 去除第 1 行 (索引为0的行)
            content_lines = lines[1:]
            
            # 将剩余行合并为字符串
            file_text = "".join(content_lines)

            # 新增: 移除 <think>...</think> 内容块
            # 使用非贪婪匹配处理多行内容
            file_text = re.sub(r'<think>.*?</think>', '', file_text, flags=re.DOTALL)
            
            # 2. 移除代码块 (``` ... ```)
            # 使用非贪婪匹配处理多行内容
            file_text = re.sub(r'```.*?```', '', file_text, flags=re.DOTALL)
            
            # 3. 去除 **、# 和 --- (在移除思考块后进行)
            clean_text = file_text.replace('**', '').replace('#', '').replace('---', '')
            
            # 收集处理后的文本
            processed_contents.append(clean_text)
            
        except Exception as e:
            print(f"读取文件 {filename} 时发生错误: {e}")

    if not processed_contents:
        print("错误: 没有找到任何可处理的文件。程序终止。")
        return None

    # 4. 合并文件并增加分隔符
    # 分隔符要求：空行、分割线、空行 (即 \n\n---\n\n)
    separator = "\n\n---\n\n"
    
    # 使用 join 将所有文件内容用分隔符连接起来
    final_merged_content = separator.join(processed_contents)

    # 5. 写入合并后的文件
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(final_merged_content)
        print(f"合并完成！中间结果已保存为: {output_filename}")
        return output_filename
    except Exception as e:
        print(f"写入合并文件时发生错误: {e}")
        return None


# ==========================================
# 第二部分：来自 itm.py (格式化处理逻辑)
# ==========================================

def step1_replace_numbers(content):
    """
    步骤一：处理 Markdown 题号
    1. 用 '---' 分割内容。
    2. 在每个片段中，将行首的数字+点替换为 \item。
    3. 重新拼接片段（相当于删除 ---）。
    """
    segments = content.split('---')
    processed_segments = []

    for segment in segments:
        lines = segment.splitlines(keepends=True)
        replaced = False
        
        for i, line in enumerate(lines):
            if not replaced:
                # 正则匹配：行首空白 + 数字 + 点
                match = re.match(r'^(\s*)(\d+)\.', line)
                
                if match:
                    # 替换为 \item，保留原有的缩进
                    lines[i] = re.sub(r'^(\s*)(\d+)\.', r'\1\\item', line)
                    replaced = True # 标记已替换，避免同一题内被误伤
        
        processed_segments.append(''.join(lines))

    return '\n'.join(processed_segments)

def step2_format_lists(content):
    """
    步骤二：格式化列表项
    """
    lines = content.splitlines(keepends=True)
    output_lines = []
    in_math_env = False

    for line in lines:
        # --- 1. 更新数学环境状态 ---
        if "$$" in line:
            in_math_env = not in_math_env
        if r"\[" in line:
            in_math_env = True
        if r"\]" in line:
            in_math_env = False

        # --- 2. 判断是否是需要处理的列表项 ---
        stripped_line = line.lstrip()
        
        # 判断 A: 无序列表
        is_separator = stripped_line.replace('-', '').replace(' ', '').strip() == ''
        is_unordered_list = stripped_line.startswith('-') and not is_separator

        # 判断 B: 有序列表
        is_ordered_list = re.match(r'^\d+\.\s+', stripped_line) is not None

        # 只要满足 A 或 B，且不在数学环境中
        is_target_list = (is_unordered_list or is_ordered_list) and not in_math_env

        # --- 3. 添加内容 ---
        if is_target_list:
            if output_lines and output_lines[-1] != "\n":
                output_lines.append("\n")
            output_lines.append(line)
            output_lines.append("\n")
        else:
            output_lines.append(line)

    return "".join(output_lines)

def format_content(input_filename):
    """
    读取输入文件，执行格式化，保存结果。
    返回 True 表示成功，False 表示失败。
    """
    print(f"\n--- 阶段 2: 格式化处理 {input_filename} ---")
    
    # 确定输出文件名
    base_name = os.path.basename(input_filename)
    output_filename = "p_" + base_name
    
    # 检查输出文件是否已存在
    if os.path.exists(output_filename):
        # 为了流程顺畅，这里直接覆盖或简单提示，也可以选择询问
        # 这里选择简单确认一下
        print(f"注意: 文件 '{output_filename}' 已存在，将被覆盖。")

    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"正在处理: {input_filename} ...")

        # 执行步骤一
        print(" [1/2] 正在转换题号格式并移除分割线...")
        content = step1_replace_numbers(content)

        # 执行步骤二
        print(" [2/2] 正在调整列表间距...")
        content = step2_format_lists(content)

        # 写入文件
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"格式化成功！最终结果已保存到: {output_filename}")
        return True

    except Exception as e:
        print(f"格式化过程中发生错误: {e}")
        return False

# ==========================================
# 主程序入口
# ==========================================

def main():
    print("========================================")
    print("   自动化合并与格式化工具 (一体化)      ")
    print("========================================")

    # 步骤 1: 运行合并逻辑
    merged_file = merge_files()

    # 步骤 2: 如果合并成功，运行格式化逻辑
    if merged_file and os.path.exists(merged_file):
        format_content(merged_file)
        print("\n========================================")
        print("   所有流程执行完毕！")
        print("========================================")
    else:
        print("\n合并阶段失败或无文件生成，跳过格式化阶段。")

if __name__ == "__main__":
    main()