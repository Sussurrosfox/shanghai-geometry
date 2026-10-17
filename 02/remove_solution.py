import re
import os

def remove_solution_blocks():
    # 1. 交互地询问要处理的文件名（不加 .md），直接回车默认处理 p_merged.md
    filename = input("请输入要处理的文件名（不加 .md），直接回车默认处理 p_merged.md：").strip()
    if not filename:
        filename = "p_merged"
    
    input_file = f"{filename}.md"
    output_file = f"{filename}_solfree.md"

    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：文件 '{input_file}' 不存在。")
        return

    try:
        # 2. 读取文件内容 (使用 utf-8 编码以支持中文)
        # Python 默认在文本模式下会将不同平台的换行符统一为 \n
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 3. 使用正则表达式删除 \begin{solution} 和 \end{solution} 之间的内容
        # flags=re.DOTALL 确保 . 可以匹配换行符
        pattern = r'\\begin\{solution\}.*?\\end\{solution\}'
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)

        # 4. 新增功能：将三行及以上行数的空行合并为一行空行
        # 逻辑说明：
        # 在文本中，视觉上的“一行空行”通常由两个换行符 (\n\n) 构成。
        # “三行及以上空行”意味着出现了 3 个或更多连续的换行符 (\n\n\n...)。
        # 此处将 3 个或更多的连续换行符替换为 2 个换行符 (\n\n)，即只保留一个视觉空行。
        new_content = re.sub(r'\n{3,}', '\n\n', new_content)

        # 5. 将处理后的内容保存到新文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"处理完成！文件已保存为：{output_file}")

    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    remove_solution_blocks()