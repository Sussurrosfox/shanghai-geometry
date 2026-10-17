"""normalize_math.py - 数学公式兼容与规范化处理脚本。

处理原则：
1. 保留公式语义，不做破坏性改写；
2. 修复双重转义宏（如 \\\\triangle -> \\triangle，\\\\perp -> \\perp，同时保留公式换行 \\\\）；
3. 转换 KaTeX / Pandoc 历史非标准宏：
   - \\bigtriangleup -> \\triangle
   - \\ang -> \\angle
   - \\parallelogram -> \\mathbin{/\\!/}
   - \\bot -> \\perp (更标准的几何垂直符号)
4. 清理正文中残余的 [cite: N] 模型引用标签；
5. 输出警告日志。
"""

import re
from typing import Tuple, List

def normalize_math_text(text: str, filename: str = "") -> Tuple[str, List[str]]:
    warnings = []
    
    # 1. 清理 LLM 生成的 [cite: N] 标签
    text = re.sub(r'\[cite:\s*\d+\]', '', text)
    
    # 2. 修复双重转义的 LaTeX 命令，例如 \\triangle -> \triangle
    # 注意：仅替换紧随英文字母的双反斜杠，保留公式末尾换行的 \\ (后接换行或空格)
    text = re.sub(r'\\\\([a-zA-Z]+)', r'\\\1', text)
    
    # 3. 宏替换
    replacements = [
        (r'\\bigtriangleup', r'\\triangle'),
        (r'\\ang(?=[^a-zA-Z]|$)', r'\\angle'),
        (r'\\parallelogram', r'\\mathbin{/\\!/}'),
        (r'\\bot(?=[^a-zA-Z]|$)', r'\\perp'),
    ]
    
    for pat, rep in replacements:
        text, n = re.subn(pat, rep, text)
    
    # 4. 检查未闭合的数学公式符号（排除 \$ 转义）
    stripped = re.sub(r'\\\$', '', text)
    dollar_count = stripped.count('$')
    if dollar_count % 2 != 0:
        warnings.append(f"[{filename}] 警告: 发现奇数个 $ 符号 ({dollar_count} 个)，可能存在未闭合的公式")
        
    return text, warnings

if __name__ == "__main__":
    sample = r"已知 $O$ 为 $\\bigtriangleup {ABC}$ 内一点，满足 ${OD} \\bot {BC}$，\\ang A。[cite: 1] 方程组: $\begin{cases} x=1 \\ y=2 \end{cases}$"
    res, w = normalize_math_text(sample, "test")
    print("Before:", sample)
    print("After :", res)
    print("Warnings:", w)
