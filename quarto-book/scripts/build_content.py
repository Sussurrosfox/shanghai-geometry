"""build_content.py - Quarto Book 自动生成器

严格遵循 design.md 与原书架构：
1. 读取 data/chapters.yml（涵盖 01, 02, 03, 04, 05, 06, 07, 08）；
2. 讲座章节（01, 02, 03, 04, 06, 07, 08）：提取知识精讲与例题（含分析、分步证明、动态演示）；
3. 习题章节（05 练习一）：提取 39 道综合习题与标准解答，并通过双图拆分算法将原书切片图片 100% 精确归位到各题；
4. 规范化公式与路径，剔除重复题头和生成提示语；
5. 去除段落意外缩进（防 Pandoc 误识别为代码块导致公式不渲染）；
6. 生成各章 index.qmd、各题 problems/NN.qmd，复制图片与演示；
7. 生成并更新 data/problems.yml 与 _quarto.yml 导航。
"""

import os
import sys
import re
import shutil
import yaml
from pathlib import Path

# 引入数学规范化模块
try:
    from normalize_math import normalize_math_text
except ImportError:
    from scripts.normalize_math import normalize_math_text

def strip_unintended_indentation(text: str) -> str:
    """清除段落首部意外的多余缩进（防止被 Pandoc 误识别为缩进代码块导致公式不被 KaTeX 渲染）"""
    lines = text.splitlines()
    new_lines = []
    in_fenced_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fenced_code = not in_fenced_code
            new_lines.append(line)
            continue
        if in_fenced_code:
            new_lines.append(line)
        else:
            if line.startswith("   "):
                new_lines.append(line.lstrip())
            else:
                new_lines.append(line)
    return "\n".join(new_lines)

def clean_problem_title(raw_first_line: str, sol_text: str, ch: str, n: int) -> str:
    """提取精炼的题目短标题（纯中文，避免 YAML 转义异常）"""
    specific_titles = {
        ("01", 2): "中位线与斜边中线构造全等（证明角相等）",
        ("01", 3): "直线 KL 过线段 AJ 的中点",
        ("01", 4): "角平分线与平行线构造全等（证明线段相等）",
        ("01", 5): "翻折与中位线构造全等",
        ("01", 6): "凸五边形垂线构造与垂心转换",
        ("01", 7): "凸六边形等长对边与旋转全等",
        ("01", 8): "中点外接圆与垂足共线证明",
        ("01", 9): "角三等分线与莫利正三角形构造",
        ("02", 2): "两圆外公切线与割线共圆及垂直证明",
        ("02", 3): "共轭相似与反交平行线角度转换",
        ("02", 4): "伴生相似与四边形角相等证明",
        ("02", 5): "双重三角形局部相似到整体相似",
        ("02", 6): "凸四边形双子相似与共圆导角",
        ("02", 7): "外心与内心连线上的线段等长证明",
        ("02", 8): "凸四边形内点等角与相似构型",
        ("03", 2): "帕斯卡定理（圆内接六边形对边交点共线）",
        ("03", 3): "圆上三点切线交点与三线共点",
        ("03", 4): "直线定点调和共轭与角平分线",
        ("03", 5): "塞瓦定理角元形式与垂心共点充要条件",
        ("03", 6): "四边形外接圆与交点线共点证明",
        ("03", 7): "六边形相交弦比例与相似三角形",
        ("03", 8): "外心、垂心反射与西姆松线共线",
        ("03", 9): "欧拉线与内心、重心、外心共线",
        ("04", 2): "旋转变换与中点线段不等式",
        ("04", 3): "圆外接三角形旋转位似",
        ("04", 4): "重心坐标与平行四边形中点对称",
        ("04", 5): "正三角形旋转与角相等证明",
        ("04", 6): "翻折对称与平行四边形判定",
        ("04", 7): "等腰三角形旋转全等与线段关系",
        ("04", 8): "两三角形同向旋转相似中心",
        ("04", 9): "中心对称构造与线段不等式极值",
        ("05", 1): "圆截三角形各边垂线共点证明",
        ("05", 2): "等腰三角形内角与线段等长证明",
        ("05", 3): "菱形外接圆与三点共线证明",
        ("05", 4): "角平分线与外接圆比例线段",
        ("05", 5): "梯形两切圆与对角线三线共点",
        ("05", 6): "锐角三角形垂心与三线共点",
        ("05", 7): "中线割线截线段倒数和比例关系",
        ("05", 8): "内切圆切点连线与等角证明",
        ("05", 9): "三个正三角形与正三角形构造",
        ("05", 10): "平行四边形高线与垂心距离计算",
        ("05", 11): "直角三角形等角与线段二倍关系",
        ("05", 12): "凸五边形等角与对角线平分",
        ("05", 13): "直角三角形斜边中点与角二倍关系",
        ("05", 14): "两圆相交与中点垂直证明（直角）",
        ("05", 15): "四点共圆割线比例与等长充要条件",
        ("05", 16): "三角形垂足连线与角平分线充要条件",
        ("05", 17): "平行四边形割线截线段等长证明",
        ("05", 18): "帕普斯定理（两直线上六点三点共线）",
        ("05", 19): "内心外接圆与垂直证明",
        ("05", 20): "凸六边形折线距离不等式证明",
        ("05", 21): "正方形内动点距离和最小值",
        ("05", 22): "平行四边形动割线旁心定角证明",
        ("05", 23): "中点与等长线段证明",
        ("05", 24): "共圆动割线与共线证明",
        ("05", 25): "外作正方形高线三线共点证明",
        ("05", 26): "相似三角形构型与三点共线证明",
        ("05", 27): "完全四边形牛顿线（对角线中点共线）",
        ("05", 28): "内切圆切点连线与外接圆定角求解",
        ("05", 29): "凸四边形特殊线段等长与角度求解",
        ("05", 30): "圆内接四边形角度转换与求值",
        ("05", 31): "圆弧中点平行线与内心共线证明",
        ("05", 32): "凸四边形中点割线等角证明",
        ("05", 33): "凸四边形垂线与等角证明",
        ("05", 34): "外接圆弧中点与内心垂直证明",
        ("05", 35): "外接圆中点与内切圆切点垂直证明",
        ("05", 36): "中点与三角形边长不等式证明",
        ("05", 37): "内切圆切点与三线共点证明",
        ("05", 38): "内切圆割线截线段比例证明",
        ("05", 39): "角平分线射影与中点平分证明",
        ("06", 2): "圆切线弦切角与内心性质证明",
        ("06", 3): "割线定理与圆内接四边形导角",
        ("06", 4): "四点共圆判定与托勒密定理应用",
        ("06", 5): "两圆相交与四点共圆综合证明",
        ("06", 6): "双圆交点与共圆四边形垂直证明",
        ("06", 7): "外心内心对称轴与线段等长",
        ("06", 8): "阿波罗尼斯圆与角度相等证明",
        ("06", 9): "共轴圆与四点共圆判定",
        ("06", 10): "圆切线与角平分线交点共线",
        ("07", 2): "两圆公共弦与根轴性质",
        ("07", 3): "相交弦定理与平行四边形判定",
        ("07", 4): "切线长定理与圆幂等长证明",
        ("07", 5): "圆内接四边形对角线根轴与共线",
        ("07", 6): "动点切线与定点定直线根轴",
        ("07", 7): "共轴圆系三线共点证明",
        ("07", 8): "垂心与外心圆幂恒等式",
        ("07", 9): "根心性质与三角形高线垂足共圆",
        ("07", 10): "反演圆与正交圆幂性质",
        ("08", 2): "内切圆切点连线与位似平行证明",
        ("08", 3): "双圆外位似中心与直角三角形证明",
        ("08", 4): "四圆共点与位似变换相似",
        ("08", 5): "调和线束与内切圆切点角平分线",
        ("08", 6): "反演变换与圆过定点证明",
        ("08", 7): "费尔巴哈定理（九点圆与内切圆切点反演）",
        ("08", 8): "外切四边形反演与调和四边形",
    }
    
    if (ch, n) in specific_titles:
        return specific_titles[(ch, n)]
    
    # 清洗掉数学公式符号
    clean_line = re.sub(r'\$.*?\$', '', raw_first_line)
    clean_line = re.sub(r'\\(?:angle|bigtriangleup|triangle|perp|sim|cong|parallel)', '', clean_line)
    clean_line = re.sub(r'^(?:例|第)?\s*\d+\s*(?:题)?[:：\.]?\s*', '', clean_line).strip()
    return clean_line[:20] if clean_line else f"第 {n} 题"

def build_ch05_image_map(ch05_dir: Path) -> dict:
    """建立练习一各题与图片的精准映射"""
    img_map = {}
    for i in range(1, 40):
        f = ch05_dir / f"{i}.md"
        if f.exists():
            txt = f.read_text(encoding='utf-8')
            matches = re.findall(r'(!\[.*?\]\((images/.*?)\))\s*\n+第\s*(\d+)\s*题', txt)
            for img_tag, img_path, prob_num in matches:
                img_map[int(prob_num)] = img_path
    return img_map

def extract_lesson_content(raw_split_file: Path, raw_file: Path) -> str:
    """从 raw_split.md 或 raw.md 中提取知识精讲部分"""
    target_file = raw_split_file if raw_split_file.exists() else raw_file
    if not target_file.exists():
        return "本讲主要介绍本专题的核心几何概念、判定定理与解题思路。"
    
    with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    start_pos = text.find("## 知识精讲")
    if start_pos == -1:
        start_pos = text.find("# 知识精讲")
    if start_pos == -1:
        m = re.search(r'例\s*1\b', text)
        if m:
            content = text[:m.start()].strip()
            lines = content.splitlines()
            if lines and lines[0].startswith('#'):
                lines = lines[1:]
            return "\n".join(lines).strip()
        return "本讲主要介绍本专题的核心几何概念与判定定理。"
    
    after_start = text[start_pos:]
    m_end = re.search(r'(?:##\s*典型例题|#\s*典型例题|\n---\s*\n|例\s*1\b)', after_start[10:])
    if m_end:
        end_pos = 10 + m_end.start()
        lesson_raw = after_start[:end_pos].strip()
    else:
        lesson_raw = after_start.strip()
    
    lesson_raw = re.sub(r'^#+\s*知识精讲\s*', '', lesson_raw).strip()
    return lesson_raw

def parse_problem_md(file_path: Path, ch_id: str, n: int, ch05_img_map: dict):
    """解析 n.md 得到题目、原书解答与图片，剔除提示语和重复题头"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tail_patterns = [
        r'这是一个费解的证明[^\n]*',
        r'我能确认每一步的正确性[^\n]*',
        r'请为我解释[^\n]*',
    ]
    for pat in tail_patterns:
        content = re.sub(pat, '', content)
    
    m_proof = re.search(r'(?:^|\n)(?:证明|解答|【证明】|【解答】)\s*', content)
    if m_proof:
        problem_part = content[:m_proof.start()].strip()
        solution_part = content[m_proof.start():].strip()
        solution_part = re.sub(r'^(?:证明|解答|【证明】|【解答】)\s*', '', solution_part).strip()
    else:
        parts = content.strip().split('\n\n', 1)
        problem_part = parts[0].strip()
        solution_part = parts[1].strip() if len(parts) > 1 else ""
    
    problem_part = re.sub(r'^(?:例|例题|第)\s*\d+[\s:：\.、题]*', '', problem_part.strip())
    
    # 针对练习一做精准图片提取与归位
    if ch_id == '05':
        # 移除解答中混杂的全部图片与题目标签
        solution_part = re.sub(r'!\[.*?\]\(images/.*?\)', '', solution_part)
        solution_part = re.sub(r'第\s*\d+\s*题', '', solution_part).strip()
        if n in ch05_img_map:
            assigned_img = ch05_img_map[n]
            # 统一加上规范相对路径
            solution_part += f"\n\n![]({assigned_img})"
    
    problem_part = strip_unintended_indentation(problem_part)
    solution_part = strip_unintended_indentation(solution_part)
    
    problem_part = re.sub(r'\]\(images/', '](../images/', problem_part)
    solution_part = re.sub(r'\]\(images/', '](../images/', solution_part)
    
    return problem_part, solution_part

def parse_solution_md(file_path: Path) -> str:
    """解析 n_solution.md 得到深度解题分析"""
    if not file_path.exists():
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    m = re.search(r'\\begin\{solution\}(.*?)\\end\{solution\}', text, re.DOTALL)
    if m:
        body = m.group(1).strip()
    else:
        if '---' in text:
            parts = text.split('---', 1)
            body = parts[1].strip()
        else:
            body = text.strip()
            
    body = strip_unintended_indentation(body)
    body = re.sub(r'\]\(images/', '](../images/', body)
    return body

def parse_steps_md(n_steps_file: Path, steps_file: Path) -> str:
    """解析 n_steps.md 或 steps.md 得到分步证明文字"""
    target_f = n_steps_file if n_steps_file.exists() else steps_file
    if not target_f or not target_f.exists():
        return ""
    with open(target_f, 'r', encoding='utf-8') as f:
        text = f.read()
        
    text = re.sub(r'^#\s+.*?\n', '', text).strip()
    text = re.sub(r'^##\s+步骤', '### 步骤', text, flags=re.MULTILINE)
    text = strip_unintended_indentation(text)
    text = re.sub(r'\]\(images/', '](../images/', text)
    return text

def build_book(project_root: Path):
    """全流程构建 Quarto Book 内容"""
    qb_dir = project_root / "quarto-book"
    data_dir = qb_dir / "data"
    chapters_yml_file = data_dir / "chapters.yml"
    
    with open(chapters_yml_file, 'r', encoding='utf-8') as f:
        chapters_data = yaml.safe_load(f)
        
    problems_metadata = []
    quarto_chapters_nav = ["index.qmd"]
    
    ch05_img_map = build_ch05_image_map(project_root / "05")
    print(f"Loaded {len(ch05_img_map)} image mappings for Chapter 05 (练习一)")
    
    print(f"Loaded {len(chapters_data)} chapters from {chapters_yml_file}")
    
    for ch_info in chapters_data:
        ch_id = ch_info['id']
        ch_num = ch_info.get('number', 1)
        ch_type = ch_info.get('type', 'lecture')
        ch_title = ch_info['title']
        lecture_num = ch_info.get('lecture_num')
        
        src_ch_dir = project_root / ch_id
        dst_ch_dir = qb_dir / "chapters" / ch_id
        dst_probs_dir = dst_ch_dir / "problems"
        dst_imgs_dir = dst_ch_dir / "images"
        dst_demos_dir = dst_ch_dir / "demos"
        
        dst_probs_dir.mkdir(parents=True, exist_ok=True)
        dst_imgs_dir.mkdir(parents=True, exist_ok=True)
        dst_demos_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. 复制所有图片
        src_imgs_dir = src_ch_dir / "images"
        if src_imgs_dir.exists():
            for img_f in src_imgs_dir.glob("*.*"):
                shutil.copy2(img_f, dst_imgs_dir / img_f.name)
                
        # 2. 知识精讲
        if ch_type == 'lecture':
            lesson_text = extract_lesson_content(src_ch_dir / "raw_split.md", src_ch_dir / "raw.md")
            lesson_norm, _ = normalize_math_text(lesson_text, f"{ch_id}/lesson.qmd")
            lesson_norm = strip_unintended_indentation(lesson_norm)
            lesson_norm = re.sub(r'\]\(\.\./images/', '](images/', lesson_norm)
            with open(dst_ch_dir / "lesson.qmd", 'w', encoding='utf-8') as f:
                f.write(lesson_norm + "\n")
        else:
            with open(dst_ch_dir / "lesson.qmd", 'w', encoding='utf-8') as f:
                f.write("本模块为前四讲知识的系统综合演练，重点训练全等变换、比例线段、共线共点与几何变换的综合运用能力。\n")

        # 3. 处理本章全部题目
        prob_files = sorted([f for f in src_ch_dir.glob('*.md') if re.match(r'^\d+\.md$', f.name)],
                            key=lambda x: int(x.stem))
        
        ch_problem_entries = []
        ch_qmd_files = [f"chapters/{ch_id}/index.qmd"]
        
        part_display_name = f"第 {lecture_num} 讲 {ch_title}" if ch_type == 'lecture' else ch_title
        
        for pf in prob_files:
            n = int(pf.stem)
            n_str = f"{n:02d}"
            prob_id = f"ch{ch_id}-p{n_str}"
            
            prob_part, sol_part = parse_problem_md(pf, ch_id, n, ch05_img_map)
            anal_part = parse_solution_md(src_ch_dir / f"{n}_solution.md")
            steps_part = parse_steps_md(src_ch_dir / str(n) / f"{n}_steps.md", src_ch_dir / str(n) / "steps.md")
            
            src_demo = src_ch_dir / str(n) / f"{n}.html"
            has_demo = src_demo.exists()
            if has_demo:
                shutil.copy2(src_demo, dst_demos_dir / f"{n_str}.html")
                
            clean_title = clean_problem_title(prob_part.splitlines()[0] if prob_part else "", anal_part, ch_id, n)
            prefix = "例" if ch_type == 'lecture' else "练习"
            full_title = f"{prefix} {n}：{clean_title}"
            safe_title = full_title.replace("'", "''")
            
            prob_part_norm, _ = normalize_math_text(prob_part, f"{prob_id}-prob")
            sol_part_norm, _ = normalize_math_text(sol_part, f"{prob_id}-sol")
            anal_part_norm, _ = normalize_math_text(anal_part, f"{prob_id}-anal") if anal_part else ("", [])
            steps_part_norm, _ = normalize_math_text(steps_part, f"{prob_id}-steps") if steps_part else ("", [])
            
            m_img = re.search(r'\!\[.*?\]\((.*?)\)', prob_part_norm + "\n" + sol_part_norm)
            main_img = m_img.group(1) if m_img else ""
            
            tags = [ch_title]
            if "中点" in prob_part_norm or "中点" in sol_part_norm: tags.append("中点")
            if "角平分线" in prob_part_norm or "角平分线" in sol_part_norm: tags.append("角平分线")
            if "共圆" in prob_part_norm or "共圆" in sol_part_norm: tags.append("四点共圆")
            if "相似" in prob_part_norm or "相似" in sol_part_norm: tags.append("相似")
            if "切线" in prob_part_norm or "切线" in sol_part_norm: tags.append("切线")
            if "根轴" in prob_part_norm or "根轴" in sol_part_norm: tags.append("根轴")
            if "反演" in prob_part_norm or "反演" in sol_part_norm: tags.append("反演")
            
            meta_record = {
                "id": prob_id,
                "chapter": ch_id,
                "problem": n,
                "type": ch_type,
                "title": clean_title,
                "tags": tags[:3],
                "difficulty": "竞赛",
                "theorems": [ch_title],
                "demo": has_demo
            }
            if main_img:
                meta_record["image"] = main_img
            if has_demo:
                meta_record["demo_path"] = f"../demos/{n_str}.html"
            
            problems_metadata.append(meta_record)
            ch_problem_entries.append((n, n_str, clean_title, meta_record))
            ch_qmd_files.append(f"chapters/{ch_id}/problems/{n_str}.qmd")
            
            # 生成各个模块 callout
            extra_blocks = []
            if anal_part_norm:
                extra_blocks.append(f"""## 解题思路与分析

::: {{.callout-note title="思路还原与分析" collapse="false"}}
{anal_part_norm}
:::""")
            if steps_part_norm:
                extra_blocks.append(f"""## 分步证明

::: {{.callout-tip title="分步推理与几何步骤" collapse="false"}}
{steps_part_norm}
:::""")
            if has_demo:
                extra_blocks.append(f"""## 动态演示

::: {{.demo-link-container}}
[在新窗口打开交互式分步演示](../demos/{n_str}.html){{.demo-link target="_blank" rel="noopener"}}
:::

<div class="demo-frame">
  <iframe src="../demos/{n_str}.html" title="{full_title} 分步演示" loading="lazy"></iframe>
</div>""")

            extra_content = "\n\n".join(extra_blocks)
            
            badge_title = part_display_name
            qmd_content = f"""---
title: '{safe_title}'
chapter: {ch_num}
problem: {n}
source-chapter: '{ch_id}'
source-file: '{ch_id}/{n}.md'
id: '{prob_id}'
tags:
{yaml.dump(tags[:3], default_flow_style=False, allow_unicode=True).strip()}
difficulty: '竞赛'
---

::: {{.problem-meta-bar}}
<span class="problem-meta-badge badge-chapter">{badge_title}</span>
<span class="problem-meta-badge badge-difficulty">竞赛难度</span>
{' '.join([f'<span class="problem-meta-badge badge-tag">{t}</span>' for t in tags[:3]])}
:::

## 题目

{prob_part_norm}

## 参考解答

::: {{.callout-important title="标准解答" collapse="false"}}
{sol_part_norm}
:::

{extra_content}
"""
            out_qmd = dst_probs_dir / f"{n_str}.qmd"
            with open(out_qmd, 'w', encoding='utf-8') as f:
                f.write(qmd_content)
                
        # 5. 生成章节 index.qmd
        table_rows = []
        for n, n_str, clean_title, mrec in ch_problem_entries:
            demo_link = f"[打开演示](demos/{n_str}.html)" if mrec['demo'] else "静态图解"
            methods = "、".join(mrec['tags'][1:]) if len(mrec['tags']) > 1 else ch_title
            prefix = "例" if ch_type == 'lecture' else "练习"
            table_rows.append(f"| [{prefix} {n}](problems/{n_str}.qmd) | {clean_title} | {methods} | {demo_link} |")
            
        index_table = "\n".join(table_rows)
        
        if ch_type == 'lecture':
            ch_index_content = f"""---
title: '{part_display_name}'
number: {lecture_num}
---

## 本讲内容

本讲系统讲解**{ch_title}**的核心理论、关键性质与竞赛突破方法。

## 知识精讲

{{{{< include lesson.qmd >}}}}

## 典型例题

| 题号 | 主题 | 核心方法 | 动态演示 |
|:---|:---|:---|:---|
{index_table}
"""
        else:
            ch_index_content = f"""---
title: '{ch_title}'
number: {ch_num}
---

## 模块介绍

本模块汇集了前四讲（全等、相似、共线共点与几何变换）的**综合竞赛提高习题**，共包含 39 道精选题例及完整详析，旨在帮助读者打通各大专题知识脉络，强化综合几何推理与证明技巧。

## 习题导引

| 题号 | 主题 | 涉及领域 | 图解模式 |
|:---|:---|:---|:---|
{index_table}
"""
        with open(dst_ch_dir / "index.qmd", 'w', encoding='utf-8') as f:
            f.write(ch_index_content)
            
        # 组装本章在 _quarto.yml 中的导航树
        quarto_chapters_nav.append({
            "part": part_display_name,
            "chapters": ch_qmd_files
        })
        
        print(f"Chapter {ch_id} ({ch_title}) completed: {len(prob_files)} problems generated.")

    # 写入 data/problems.yml
    problems_yml_file = data_dir / "problems.yml"
    with open(problems_yml_file, 'w', encoding='utf-8') as f:
        yaml.dump(problems_metadata, f, default_flow_style=False, allow_unicode=True)
    print(f"Successfully generated {problems_yml_file} with {len(problems_metadata)} problems.")

    # 更新 _quarto.yml
    quarto_yml_file = qb_dir / "_quarto.yml"
    quarto_config = {
        "project": {
            "type": "book",
            "output-dir": "_site",
            "resources": [
                "chapters/**/images/**",
                "chapters/**/demos/**"
            ]
        },
        "execute": {
            "freeze": True,
            "echo": False
        },
        "lang": "zh",
        "book": {
            "title": "上海中学竞赛课程：平面几何",
            "author": "上海中学竞赛课程",
            "language": "zh",
            "search": True,
            "chapters": quarto_chapters_nav
        },
        "format": {
            "html": {
                "theme": [
                    "cosmo",
                    "assets/book.scss"
                ],
                "toc": True,
                "toc-depth": 3,
                "html-math-method": "katex",
                "include-in-header": "assets/katex-macros.html",
                "smooth-scroll": True
            },
            "pdf": {
                "pdf-engine": "xelatex",
                "documentclass": "ctexbook",
                "classoption": ["UTF8", "oneside"],
                "geometry": ["a4paper", "margin=20mm"],
                "include-in-header": "assets/macros.tex",
                "toc": True
            }
        }
    }
    
    with open(quarto_yml_file, 'w', encoding='utf-8') as f:
        yaml.dump(quarto_config, f, default_flow_style=False, allow_unicode=True)
    print(f"Successfully updated {quarto_yml_file}")

if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent.parent
    build_book(root)
