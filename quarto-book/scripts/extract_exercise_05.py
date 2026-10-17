# -*- coding: utf-8 -*-
"""
extract_exercise_05.py - 提取练习一（习题模块 05）的题目、解答与图片

从 book_2 根目录下的 05_练习一.md 和 15_参考答案.md 中提取 39 道习题及其解答，
并写入 chapters/05/ 目录。
"""

import os
import re
import shutil
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    qb_dir = script_dir.parent
    chapters_dir = qb_dir.parent
    book2_dir = chapters_dir.parent

    # 寻找文件
    ex_file = None
    for f in book2_dir.glob("*05*练习一*.md"):
        ex_file = f
        break
    if not ex_file:
        for f in book2_dir.glob("*05*.md"):
            ex_file = f
            break

    ans_file = None
    for f in book2_dir.glob("*15*参考答案*.md"):
        ans_file = f
        break
    if not ans_file:
        for f in book2_dir.glob("*15*.md"):
            ans_file = f
            break

    print(f"Exercise file: {ex_file}")
    print(f"Answer file: {ans_file}")

    if not ex_file or not ans_file:
        print("Error: Could not locate 05 or 15 files!")
        return

    with open(ex_file, 'r', encoding='utf-8') as f:
        ex_text = f.read()

    with open(ans_file, 'r', encoding='utf-8') as f:
        ans_text = f.read()

    pos1 = ans_text.find("## 练习一")
    pos2 = ans_text.find("## 练习二")
    ans_ex1 = ans_text[pos1:pos2] if pos2 != -1 else ans_text[pos1:]

    # 正则提取题目
    prob_matches = list(re.finditer(r'(?:^|\n)(\d+)\.\s*(.*?)(?=(?:\n\d+\.|\Z))', ex_text, re.DOTALL))
    ans_matches = list(re.finditer(r'(?:^|\n)(\d+)\.\s*(.*?)(?=(?:\n\d+\.|\Z))', ans_ex1, re.DOTALL))

    probs = {int(m.group(1)): m.group(2).strip() for m in prob_matches}
    anss = {int(m.group(1)): m.group(2).strip() for m in ans_matches}

    print(f"Extracted {len(probs)} problems and {len(anss)} solutions.")

    # 建立 chapters/05 目录
    ch05_dir = chapters_dir / "05"
    ch05_img_dir = ch05_dir / "images"
    ch05_img_dir.mkdir(parents=True, exist_ok=True)

    book2_images = book2_dir / "images"

    # 复制练习一涉及的图片
    copied_count = 0
    for n, a_text in anss.items():
        imgs = re.findall(r'!\[.*?\]\(images/(.*?)\)', a_text)
        for img in imgs:
            src = book2_images / img
            if src.exists():
                shutil.copy2(src, ch05_img_dir / img)
                copied_count += 1
    print(f"Copied {copied_count} images to chapters/05/images")

    # 写入 1.md ~ 39.md
    for n in range(1, 40):
        p_content = probs.get(n, '')
        a_content = anss.get(n, '')
        combined = f"{p_content}\n\n证明\n\n{a_content}\n"
        with open(ch05_dir / f"{n}.md", 'w', encoding='utf-8') as f:
            f.write(combined)

    print(f"Successfully generated 39 problem files in chapters/05/")

if __name__ == "__main__":
    main()
