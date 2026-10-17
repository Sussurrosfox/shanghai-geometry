import os, sys, math, json
from generate_core import *
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# 08/2 (例 1)
# ==========================================
def build_08_2():
    os.makedirs("08/2", exist_ok=True)
    A = (320.00, 100.00)
    B = (150.00, 390.00)
    C = (490.00, 390.00)
    I = (320.00, 292.60)
    r = 97.40
    O = (320.00, 294.83)
    R = 194.83
    D = (320.00, 390.00)
    E = (404.03, 243.34)
    F = (235.97, 243.34)
    M = (488.08, 196.30)
    N = (151.92, 196.30)
    R_arc = (320.00, 489.66)
    P = (320.00, 290.37)
    X = (235.01, 340.18)
    Y = (404.99, 340.18)
    A_prime = (320.00, -90.42)
    B_prime = (-20.04, 489.66)
    C_prime = (660.04, 489.66)

    view_box = "60 30 520 480"

    base_svg = f"""
      {poly_svg([A, B, C], stroke="#1e293b", stroke_w=2.0)}
      {circle_svg(I[0], I[1], r, stroke="#0284c7", stroke_w=1.5)}
      {circle_svg(O[0], O[1], R, stroke="#64748b", stroke_w=1.2, dash="4,4", opacity=0.6)}
      {line_svg(M, E, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(N, F, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(P, B, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(P, C, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(X, Y, stroke="#e11d48", stroke_w=2.0)}
    """

    pts_svg = f"""
      {dot_svg(A, "#0f172a")} {label_svg(A, "A", 0, -10)}
      {dot_svg(B, "#0f172a")} {label_svg(B, "B", -16, 12)}
      {dot_svg(C, "#0f172a")} {label_svg(C, "C", 8, 12)}
      {dot_svg(I, "#0284c7")} {label_svg(I, "I", 8, 4, "#0284c7")}
      {dot_svg(D, "#0284c7")} {label_svg(D, "D", 0, 16, "#0284c7")}
      {dot_svg(E, "#0284c7")} {label_svg(E, "E", 10, -4, "#0284c7")}
      {dot_svg(F, "#0284c7")} {label_svg(F, "F", -16, -4, "#0284c7")}
      {dot_svg(M, "#059669")} {label_svg(M, "M", 8, 0, "#059669")}
      {dot_svg(N, "#059669")} {label_svg(N, "N", -18, 0, "#059669")}
      {dot_svg(P, "#dc2626")} {label_svg(P, "P", -14, -6, "#dc2626")}
      {dot_svg(X, "#e11d48")} {label_svg(X, "X", -16, -6, "#e11d48")}
      {dot_svg(Y, "#e11d48")} {label_svg(Y, "Y", 8, -6, "#e11d48")}
    """

    step_defs = [
        {
            "step": 0,
            "title": "已知构型与初始条件",
            "text": "设 $\\bigtriangleup ABC$ 的内切圆 $I$ 与三边切于 $D, E, F$；$M, N$ 分别为外接圆 $\\omega$ 弧 $AC, AB$ 的中点；$ME, NF$ 交于点 $P$；割线 $PB, PC$ 与圆 $I$ 分别交于点 $X, Y$。求证：$XY \\parallel BC$。",
            "svg": ""
        },
        {
            "step": 1,
            "title": "① 引入弧 $BC$ 中点 $R$ 并作外切线",
            "text": "设弧 $BC$ 的中点为 $R$，过点 $M, N, R$ 作外接圆 $\\omega$ 的切线，相交构成 $\\bigtriangleup A'B'C'$。记外心为 $O$。",
            "svg": f"""
              {dot_svg(R_arc, "#059669")} {label_svg(R_arc, "R", 0, 16, "#059669")}
              {poly_svg([A_prime, B_prime, C_prime], stroke="#059669", stroke_w=1.8, dash="5,5", opacity=0.85)}
              {line_svg(O, N, stroke="#059669", stroke_w=1.2, dash="3,3")}
              {dot_svg(O, "#64748b")} {label_svg(O, "O", 6, -6, "#64748b")}
            """
        },
        {
            "step": 2,
            "title": "② 垂径定理导出对应边平行",
            "text": "由切线性质知 $ON \\bot A'B'$；又由垂径定理知弧中点连径垂直弦，即 $ON \\bot AB$。故对应边平行：$AB \\parallel A'B'$。同理可得 $BC \\parallel B'C', CA \\parallel C'A'$。",
            "svg": f"""
              {line_svg(A, B, stroke="#2563eb", stroke_w=2.5)}
              {line_svg(A_prime, B_prime, stroke="#2563eb", stroke_w=2.5, dash="4,4")}
              {line_svg(B, C, stroke="#2563eb", stroke_w=2.5)}
              {line_svg(B_prime, C_prime, stroke="#2563eb", stroke_w=2.5, dash="4,4")}
            """
        },
        {
            "step": 3,
            "title": "③ 确立位似映射与切点对应",
            "text": "三组对应边分别平行的两三角形必存在位似变换，将 $\\bigtriangleup ABC$ 映射为 $\\bigtriangleup A'B'C'$。该位似变换将内切圆 $I$ 映射为圆 $\\omega$，各切点对应转换：$F \\to N, E \\to M, D \\to R$。",
            "svg": f"""
              {line_svg(I, F, stroke="#0284c7", stroke_w=1.8)}
              {line_svg(O, N, stroke="#059669", stroke_w=1.8)}
              {line_svg(I, E, stroke="#0284c7", stroke_w=1.8)}
              {line_svg(O, M, stroke="#059669", stroke_w=1.8)}
            """
        },
        {
            "step": 4,
            "title": "④ 连心线交点 $P$ 即位似中心",
            "text": "因为对应切点连线 $FN$ 与 $EM$ 的交点正是 $P$，由位似中心性质，对应点连线必共点于位似中心，故点 $P$ 即为两图形的位似中心！从而 $P, B, B'$ 共线，且 $P, C, C'$ 共线。",
            "svg": f"""
              {line_svg(M, E, stroke="#dc2626", stroke_w=2.0)}
              {line_svg(N, F, stroke="#dc2626", stroke_w=2.0)}
              {dot_svg(P, "#dc2626", 5.5)}
              {line_svg(P, B_prime, stroke="#d97706", stroke_w=1.5, dash="3,3")}
              {line_svg(P, C_prime, stroke="#d97706", stroke_w=1.5, dash="3,3")}
            """
        },
        {
            "step": 5,
            "title": "⑤ 变换保平行导出 $XY \\parallel BC$",
            "text": "位似变换将内切圆 $I$ 上的点 $X, Y$ 沿射线 $PB, PC$ 分别放大映射为圆 $\\omega$ 上的顶点 $B, C$。因此线段 $XY$ 与 $BC$ 互为位似对应线段，严格满足 $XY \\parallel BC$。证毕！",
            "svg": f"""
              {line_svg(X, Y, stroke="#e11d48", stroke_w=3.0)}
              {line_svg(B, C, stroke="#2563eb", stroke_w=3.0)}
              {line_svg(P, B, stroke="#dc2626", stroke_w=1.5)}
              {line_svg(P, C, stroke="#dc2626", stroke_w=1.5)}
            """
        }
    ]

    html = gen_html_template(
        "例 1：切点与弧中点的位似变换及平行线判定",
        "利用位似变换将内切圆与外接圆建立映射，证明割线弦与底边平行",
        "08/2.md",
        view_box,
        base_svg,
        pts_svg,
        step_defs
    )
    with open("08/2/2.html", "w", encoding="utf-8") as f:
        f.write(html)

    # 写入 2_steps.md
    with open("08/2/2_steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/2 步骤提取\n\n")
        for s in step_defs:
            f.write(f"## 步骤 {s['step']}：{s['title']}\n\n{s['text']}\n\n")

    print("08/2 generated successfully.")

build_08_2()
