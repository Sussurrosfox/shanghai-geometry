from pathlib import Path


def main():
    # 获取当前脚本所在目录
    script_dir = Path(__file__).parent
    method_file = script_dir / "method.txt"

    # 检查 method.txt 是否存在
    if not method_file.exists():
        print("method.txt 文件不存在")
        return

    # 读取 method.txt 内容
    try:
        method_content = method_file.read_text(encoding="utf-8").strip()
    except Exception as e:
        print(f"读取 method.txt 失败: {e}")
        return

    # 交互式询问处理文件数
    try:
        n = int(input("请输入需要处理的文件数 N: ").strip())
    except ValueError:
        print("输入无效，请输入一个正整数")
        return

    if n <= 0:
        print("N 必须是正整数")
        return

    success_count = 0
    fail_count = 0

    for k in range(1, n + 1):
        md_file = script_dir / f"{k}.md"

        # 检查 md 文件是否存在
        if not md_file.exists():
            print(f"[{k}] 文件 {k}.md 不存在，跳过")
            fail_count += 1
            continue

        # 读取原内容并追加
        try:
            original_content = md_file.read_text(encoding="utf-8")
            # 换行后追加 method 内容
            new_content = original_content.rstrip() + "\n\n" + method_content
            md_file.write_text(new_content, encoding="utf-8")
            print(f"[{k}] 成功: 已追加内容到 {k}.md")
            success_count += 1
        except Exception as e:
            print(f"[{k}] 处理失败: {e}")
            fail_count += 1

    print(f"\n处理完成: 成功 {success_count} 个，失败 {fail_count} 个")


if __name__ == "__main__":
    main()