import re
import os

def list_files():
    """列出当前文件夹中所有的 .md 和 .tex 文件"""
    files = []
    for filename in os.listdir('.'):
        if filename.endswith('.md') or filename.endswith('.tex'):
            if os.path.isfile(filename):  # 确保是文件不是目录
                files.append(filename)
    return sorted(files)  # 按字母顺序排序

def select_file(files):
    """交互式选择文件"""
    if not files:
        print("当前文件夹中没有 .md 或 .tex 文件。")
        return None
    
    print("\n=== 可用文件列表 ===")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")
    print("===================\n")
    
    while True:
        try:
            choice = input(f"请选择要处理的文件 (1-{len(files)})，或输入 'q' 退出：").strip()
            if choice.lower() == 'q':
                return None
            choice_num = int(choice)
            if 1 <= choice_num <= len(files):
                return files[choice_num - 1]
            else:
                print(f"请输入 1 到 {len(files)} 之间的数字。")
        except ValueError:
            print("输入无效，请输入数字或 'q'。")

def process_file():
    # 1. 列出并选择文件
    files = list_files()
    filename = select_file(files)
    
    if filename is None:
        print("已取消操作。")
        return
    
    # 检查文件是否存在（双重确认）
    if not os.path.exists(filename):
        print(f"错误：文件 '{filename}' 不存在。")
        return

    try:
        # 2. 读取文件内容 (默认使用 utf-8 编码)
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 3. 定义正则表达式和替换内容
        # 匹配连续 2 个或更多的下划线
        pattern = r'_{2,}'
        # 替换为 \underline{\hbox to 40mm{}}
        replacement = r'\\underline{\\hbox to 40mm{}}'
        
        # 4. 执行替换
        new_content = re.sub(pattern, replacement, content)
        
        # 5. 写回文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"\n✓ 处理完成！文件 '{filename}' 中所有连续下划线组已替换。")
        
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    process_file()