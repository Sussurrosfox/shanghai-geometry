import os

def main():
    # 1. 交互式询问要处理的文件数量 N
    try:
        user_input = input("请输入要处理的文件数量 N: ")
        n = int(user_input)
    except ValueError:
        print("错误：请输入一个有效的整数。")
        return

    if n <= 0:
        print("错误：N 必须是正整数。")
        return

    print(f"开始处理 {n} 个文件...\n")

    # 2. 循环处理每一个文件
    for k in range(1, n + 1):
        src_file = f"{k}.md"
        dst_file = f"{k}_solution.md"

        # 检查目标文件是否已存在，如果存在则跳过
        if os.path.isfile(dst_file):
            print(f"跳过：文件 '{dst_file}' 已存在。")
            continue

        # 检查源文件是否存在
        if not os.path.isfile(src_file):
            print(f"警告：文件 '{src_file}' 不存在，跳过处理。")
            continue

        try:
            # 读取原文件内容
            with open(src_file, 'r', encoding='utf-8') as f_in:
                content = f_in.read()

            # 去除内容末尾的空白字符（包括换行符），以便我们精确控制后续的空行格式
            content = content.rstrip()

            # 3. 构建新文件的内容
            
            # 第一部分：标题 ## k.md 加上两个空行
            # \n\n 代表两个换行，视觉上即标题后空两行
            header = f"## {k}.md\n\n"

            # 第二部分：原文件内容
            # (已在上文读取并赋值给 content)

            # 第三部分：尾部格式
            # 要求：（空行）（空行）（分割线）（空行）（空行）\begin{solution}（空行）（空行）\end{solution}
            # 注意：在 Python 字符串中，反斜杠 \ 需要转义，所以写为 \\
            footer = "\n\n---\n\n\\begin{solution}\n\n\\end{solution}\n"

            # 合并所有内容
            final_content = header + content + footer

            # 4. 写入新文件
            with open(dst_file, 'w', encoding='utf-8') as f_out:
                f_out.write(final_content)

            print(f"成功处理：{src_file} -> {dst_file}")

        except Exception as e:
            print(f"处理文件 '{src_file}' 时发生未知错误：{e}")

    print("\n所有任务完成。")

if __name__ == "__main__":
    main()