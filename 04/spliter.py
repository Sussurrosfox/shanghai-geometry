import os

def main():
    print("=== Markdown 题目分割工具 ===")
    
    # 1. 获取当前目录下所有 .md 文件
    try:
        all_files = os.listdir('.')
        # 过滤出 .md 文件，并确保是文件而非文件夹，同时排序
        md_files = sorted([f for f in all_files if f.endswith('.md') and os.path.isfile(f)])
    except Exception as e:
        print(f"读取目录时出错：{e}")
        return

    # 2. 列出文件供选择
    print("\n当前目录下的 .md 文件:")
    if not md_files:
        print("  (未找到任何 .md 文件)")
    else:
        for i, filename in enumerate(md_files, 1):
            print(f"  {i}. {filename}")
    
    # 3. 交互式选择
    print("\n默认文件：raw.md")
    choice = input("请输入文件编号或文件名 (直接回车使用默认): ").strip()
    
    input_file = "raw.md"  # 默认值
    
    if choice:
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(md_files):
                input_file = md_files[index]
            else:
                print(f"警告：编号 {choice} 无效，将使用默认文件 raw.md")
        else:
            input_file = choice
    
    # 4. 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：在当前目录下找不到文件 '{input_file}'。")
        print("请确认文件名是否正确或文件是否存在。")
        return

    print(f"正在读取文件：{input_file} ... ")

    try:
        # 读取文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取文件时出错：{e}")
        return

    # 5. 分割内容
    raw_problems = content.split('---')
    count = 0

    for problem in raw_problems:
        # 去除首尾空白
        clean_problem = problem.strip()

        # 跳过空内容
        if not clean_problem:
            continue

        count += 1
        output_filename = f"{count}.md"

        # 写入文件
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(clean_problem)
            print(f"已生成：{output_filename}")
        except Exception as e:
            print(f"写入文件 {output_filename} 失败：{e}")

    print("-" * 20)
    print(f"处理完成！共提取了 {count} 道题目。")

if __name__ == "__main__":
    main()