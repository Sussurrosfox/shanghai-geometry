"""validate_content.py - Quarto Book 零信任质量与安全门禁校验脚本

支持构建前(pre-check)与构建后(post-check)两阶段全维度验证：
包含 7 个讲座章节与 1 个阶段练习习题模块（共 8 个模块，95 道题目）。
"""

import sys
import os
import re
import argparse
import yaml
from pathlib import Path

def validate_pre(qb_dir: Path, src_root: Path):
    print("=" * 60)
    print(">>> 运行构建前门禁校验 (Pre-build Validation)...")
    print("=" * 60)
    
    issues = []
    
    # 1. 检查 chapters.yml
    chapters_yml = qb_dir / "data" / "chapters.yml"
    if not chapters_yml.exists():
        issues.append(f"缺失 chapters.yml 文件: {chapters_yml}")
        return False, issues
        
    with open(chapters_yml, 'r', encoding='utf-8') as f:
        chapters = yaml.safe_load(f)
        
    expected_chs = ['01', '02', '03', '04', '05', '06', '07', '08']
    ch_ids = [c['id'] for c in chapters]
    if ch_ids != expected_chs:
        issues.append(f"chapters.yml 中章节不符合要求: 发现 {ch_ids}, 期望 {expected_chs}")
        
    # 2. 统计源材料层
    total_problems = 0
    total_solutions = 0
    total_step_files = 0
    total_demos = 0
    missing_images = 0
    missing_demos = 0
    unresolved_math = 0
    
    seen_ids = set()
    
    for ch in expected_chs:
        src_ch = src_root / ch
        if not src_ch.exists():
            issues.append(f"源章节目录不存在: {src_ch}")
            continue
            
        prob_files = sorted([f for f in src_ch.glob('*.md') if re.match(r'^\d+\.md$', f.name)],
                            key=lambda x: int(x.stem))
        
        is_exercise = (ch == '05')
        
        for pf in prob_files:
            total_problems += 1
            n = pf.stem
            prob_id = f"ch{ch}-p{int(n):02d}"
            if prob_id in seen_ids:
                issues.append(f"发现重复题目 ID: {prob_id}")
            seen_ids.add(prob_id)
            
            # 检查 UTF-8 解码与公式
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.count('$') % 2 != 0:
                        unresolved_math += 1
                        issues.append(f"[{pf}] 公式分隔符 $ 数量为奇数")
            except Exception as e:
                issues.append(f"[{pf}] UTF-8 解码失败: {e}")
                
            if not is_exercise:
                # 检查 solution
                sol_f = src_ch / f"{n}_solution.md"
                if sol_f.exists():
                    total_solutions += 1
                else:
                    issues.append(f"缺失解题分析文件: {sol_f}")
                    
                # 检查 steps
                n_steps_f = src_ch / n / f"{n}_steps.md"
                steps_f = src_ch / n / "steps.md"
                if n_steps_f.exists():
                    total_step_files += 1
                if steps_f.exists():
                    total_step_files += 1
                if not n_steps_f.exists() and not steps_f.exists():
                    issues.append(f"[{ch}/{n}] 缺失 steps.md 或 n_steps.md")
                    
                # 检查 demos
                demo_f = src_ch / n / f"{n}.html"
                if demo_f.exists():
                    total_demos += 1
                else:
                    missing_demos += 1
                    issues.append(f"缺失动态演示: {demo_f}")
            else:
                total_solutions += 1
                
            # 检查图片引用
            imgs = re.findall(r'!\[.*?\]\((?:images/)?(.*?)\)', content)
            for img in imgs:
                img_path = src_ch / "images" / img
                if not img_path.exists():
                    missing_images += 1
                    issues.append(f"[{ch}/{n}] 缺失图片: {img_path}")
                    
    print("\n--- 构建前统计指标 ---")
    print(f"chapters: {len(chapters)}")
    print(f"problems: {total_problems}")
    print(f"solution_files: {total_solutions}")
    print(f"step_files: {total_step_files}")
    print(f"demos: {total_demos}")
    print(f"missing_images: {missing_images}")
    print(f"missing_demos: {missing_demos}")
    print(f"unresolved_math: {unresolved_math}")
    print("------------------------\n")
    
    if issues:
        print(f"构建前发现 {len(issues)} 处问题:")
        for iss in issues[:10]:
            print(f"  - {iss}")
        return False, issues
    else:
        print("构建前门禁校验全部通过 (PASS)！\n")
        return True, []

def validate_post(qb_dir: Path):
    print("=" * 60)
    print(">>> 运行构建后门禁校验 (Post-build Validation)...")
    print("=" * 60)
    
    site_dir = qb_dir / "_site"
    if not site_dir.exists():
        print(f"错误: _site 目录未生成: {site_dir}")
        return False, ["_site 目录缺失"]
        
    issues = []
    
    # 1. 检查 index.html
    root_index = site_dir / "index.html"
    if not root_index.exists():
        issues.append("缺失根主页 _site/index.html")
        
    # 2. 检查各章 index 与 problems
    valid_ch_count = 0
    valid_prob_count = 0
    valid_demo_count = 0
    
    expected_chs = ['01', '02', '03', '04', '05', '06', '07', '08']
    
    html_files = list(site_dir.glob("**/*.html"))
    print(f"扫描 _site 目录下共 {len(html_files)} 个 HTML 页面...")
    
    for ch in expected_chs:
        ch_idx = site_dir / "chapters" / ch / "index.html"
        if ch_idx.exists():
            valid_ch_count += 1
        else:
            issues.append(f"缺失章节主页: {ch_idx}")
            
        prob_htmls = list((site_dir / "chapters" / ch / "problems").glob("*.html"))
        valid_prob_count += len(prob_htmls)
        
        # 抽查 HTML 是否包含 KaTeX 与 callout 结构
        for ph in prob_htmls:
            try:
                with open(ph, 'r', encoding='utf-8') as f:
                    txt = f.read()
                    if "<div class=\"callout" not in txt and "<div class=\"callout-important" not in txt:
                        issues.append(f"[{ph.name}] 缺失 callout 容器结构")
                    if "katex" not in txt.lower():
                        issues.append(f"[{ph.name}] 缺失 KaTeX 渲染机制")
                    # 检查是否残留未转义的特殊语法
                    if "\\begin{align*}" in txt or "\\begin{gather*}" in txt:
                        issues.append(f"[{ph.name}] 残留未解析的 align*/gather* 环境")
            except Exception as e:
                issues.append(f"读取页面失败 {ph}: {e}")
                
        # 检查 demos
        demo_htmls = list((site_dir / "chapters" / ch / "demos").glob("*.html"))
        valid_demo_count += len(demo_htmls)

    print("\n--- 构建后验证统计指标 ---")
    print(f"valid_chapters_html: {valid_ch_count} / {len(expected_chs)}")
    print(f"valid_problems_html: {valid_prob_count} (目标: 95)")
    print(f"valid_demos_html: {valid_demo_count} (目标: 56)")
    print(f"total_issues: {len(issues)}")
    print("------------------------\n")
    
    if issues:
        print(f"构建后发现 {len(issues)} 处质量违背:")
        for iss in issues[:10]:
            print(f"  - {iss}")
        return False, issues
    else:
        print("构建后门禁校验全部通过 (PASS)！\n")
        return True, []

def main():
    parser = argparse.ArgumentParser(description="Quarto Book 质量门禁校验工具")
    parser.add_argument("--stage", choices=["pre", "post", "all"], default="all",
                        help="校验阶段：pre(构建前) | post(构建后) | all(全部)")
    args = parser.parse_args()
    
    current_dir = Path(__file__).resolve().parent.parent
    src_root = current_dir.parent
    
    success = True
    if args.stage in ["pre", "all"]:
        ok, _ = validate_pre(current_dir, src_root)
        if not ok:
            success = False
            
    if args.stage in ["post", "all"]:
        ok, _ = validate_post(current_dir)
        if not ok:
            success = False
            
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
