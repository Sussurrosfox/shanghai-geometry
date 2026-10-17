import os, sys, math, json
from generate_core import *
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

def build_08_8():
    os.makedirs("08/8", exist_ok=True)
    O = (320.00, 270.00)
    scale = 24.0 # 1 unit = 24 px
    r_val = 3.8 * scale # r approx 91.2 px

    # OA=5, OB=6, OC=7, OD=8
    d_A = 5.0 * scale
    d_B = 6.0 * scale
    d_C = 7.0 * scale
    d_D = 8.0 * scale

    # Angles around O
    ang_A = math.radians(48)
    ang_B = math.radians(132)
    ang_C = math.radians(222)
    ang_D = math.radians(312)

    A = (O[0] + d_A * math.cos(ang_A), O[1] - d_A * math.sin(ang_A))
    B = (O[0] + d_B * math.cos(ang_B), O[1] - d_B * math.sin(ang_B))
    C = (O[0] + d_C * math.cos(ang_C), O[1] - d_C * math.sin(ang_C))
    D = (O[0] + d_D * math.cos(ang_D), O[1] - d_D * math.sin(ang_D))

    # Midpoints of AC and BD
    M = ((A[0]+C[0])/2, (A[1]+C[1])/2)
    N = ((B[0]+D[0])/2, (B[1]+D[1])/2)

    # Inversion points: OA' = r^2 / OA
    r2 = r_val * r_val
    def inv_pt(P, d_orig, ang):
        d_prime = r2 / d_orig
        return (O[0] + d_prime * math.cos(ang), O[1] - d_prime * math.sin(ang))

    A_prime = inv_pt(A, d_A, ang_A)
    B_prime = inv_pt(B, d_B, ang_B)
    C_prime = inv_pt(C, d_C, ang_C)
    D_prime = inv_pt(D, d_D, ang_D)

    # Common midpoint of A'C' and B'D'
    S = ((A_prime[0]+C_prime[0])/2, (A_prime[1]+C_prime[1])/2)

    view_box = "80 40 480 460"

    base_svg = f"""
      {circle_svg(O[0], O[1], r_val, stroke="#64748b", stroke_w=1.4, dash="4,4")}
      {poly_svg([A, B, C, D], stroke="#1e293b", stroke_w=1.8)}
      {line_svg(A, C, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(B, D, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(O, M, stroke="#dc2626", stroke_w=2.2)}
      {line_svg(O, N, stroke="#2563eb", stroke_w=2.2)}
    """

    pts_svg = f"""
      {dot_svg(O, "#64748b")} {label_svg(O, "O", 6, -6, "#64748b")}
      {dot_svg(A, "#0f172a")} {label_svg(A, "A (5)", 8, -6)}
      {dot_svg(B, "#0f172a")} {label_svg(B, "B (6)", -16, -6)}
      {dot_svg(C, "#0f172a")} {label_svg(C, "C (7)", -16, 12)}
      {dot_svg(D, "#0f172a")} {label_svg(D, "D (8)", 8, 12)}
      {dot_svg(M, "#dc2626", 4.5)} {label_svg(M, "M", 6, -6, "#dc2626")}
      {dot_svg(N, "#2563eb", 4.5)} {label_svg(N, "N", -14, -6, "#2563eb")}
    """

    step_defs = [
        {
            "step": 0,
            "title": "已知构型与核心待求线段",
            "text": "设凸四边形 $ABCD$ 外切于圆 $O$，$OA=5, OB=6, OC=7, OD=8$。对角线 $AC, BD$ 的中点分别为 $M, N$。求 $\\frac{OM}{ON}$ 的值。",
            "svg": ""
        },
        {
            "step": 1,
            "title": "① 建立以 $O$ 为中心、半径 $r$ 的反演变换",
            "text": "以 $O$ 为反演中心、圆 $O$ 为基圆（反演幂 $r^2$）作反演变换。各顶点反演像 $A', B', C', D'$ 落在射线 $OA, OB, OC, OD$ 上，满足 $OA \\cdot OA' = OB \\cdot OB' = OC \\cdot OC' = OD \\cdot OD' = r^2$。",
            "svg": f"""
              {dot_svg(A_prime, "#7c3aed")} {label_svg(A_prime, "A'", 8, -4, "#7c3aed")}
              {dot_svg(B_prime, "#7c3aed")} {label_svg(B_prime, "B'", -14, -4, "#7c3aed")}
              {dot_svg(C_prime, "#7c3aed")} {label_svg(C_prime, "C'", -14, 8, "#7c3aed")}
              {dot_svg(D_prime, "#7c3aed")} {label_svg(D_prime, "D'", 8, 8, "#7c3aed")}
            """
        },
        {
            "step": 2,
            "title": "② 证明 $A'B'C'D'$ 为切点中位线平行四边形",
            "text": "由切线直角射影性质，$A', B', C', D'$ 分别为切点弦的中点。由三角形中位线定理，$A'B' \\parallel C'D'$ 且 $A'B' = C'D' = \\frac{1}{2}HF$。因此 $A'B'C'D'$ 严格为一个平行四边形！其对角线互相平分于公共中点 $S$。",
            "svg": f"""
              {poly_svg([A_prime, B_prime, C_prime, D_prime], stroke="#7c3aed", stroke_w=2.0, fill="rgba(124,58,237,0.08)")}
              {line_svg(A_prime, C_prime, stroke="#7c3aed", stroke_w=1.2, dash="3,3")}
              {line_svg(B_prime, D_prime, stroke="#7c3aed", stroke_w=1.2, dash="3,3")}
              {dot_svg(S, "#d946ef", 5)} {label_svg(S, "S", 8, -4, "#d946ef")}
              {line_svg(O, S, stroke="#7c3aed", stroke_w=1.8)}
            """
        },
        {
            "step": 3,
            "title": "③ 相似三角形中线比：表达 $OM$",
            "text": "由反演性质知 $\\bigtriangleup A'OC' \\sim \\bigtriangleup COA$（反向相似）。线段 $OS$ 与 $OM$ 分别是两相似三角形对应的中线，故对应中线比等于对应边长比：$\\frac{OS}{OM} = \\frac{OA'}{OC} = \\frac{r^2}{OA \\cdot OC}$，解得 $OM = \\frac{OS \\cdot OA \\cdot OC}{r^2}$。",
            "svg": f"""
              {poly_svg([A_prime, O, C_prime], stroke="#059669", stroke_w=1.8, fill="rgba(5,150,105,0.12)")}
              {poly_svg([C, O, A], stroke="#059669", stroke_w=1.8, fill="rgba(5,150,105,0.08)")}
              {line_svg(O, M, stroke="#dc2626", stroke_w=2.8)}
              {line_svg(O, S, stroke="#7c3aed", stroke_w=2.2)}
            """
        },
        {
            "step": 4,
            "title": "④ 相似三角形中线比：表达 $ON$",
            "text": "同理，在另一对对角线构成的三角形中，$\\bigtriangleup B'OD' \\sim \\bigtriangleup DOB$。$OS$ 与 $ON$ 为对应中线，满足：$\\frac{OS}{ON} = \\frac{OB'}{OD} = \\frac{r^2}{OB \\cdot OD}$，解得 $ON = \\frac{OS \\cdot OB \\cdot OD}{r^2}$。",
            "svg": f"""
              {poly_svg([B_prime, O, D_prime], stroke="#d97706", stroke_w=1.8, fill="rgba(217,119,6,0.12)")}
              {poly_svg([D, O, B], stroke="#d97706", stroke_w=1.8, fill="rgba(217,119,6,0.08)")}
              {line_svg(O, N, stroke="#2563eb", stroke_w=2.8)}
              {line_svg(O, S, stroke="#7c3aed", stroke_w=2.2)}
            """
        },
        {
            "step": 5,
            "title": "⑤ 比值消元，得出最终精确值 $\\frac{35}{48}$",
            "text": "将两式相除，公共未知量 $OS$ 与反演基圆幂 $r^2$ 完全对消：\n$$\\frac{OM}{ON} = \\frac{\\frac{OS \\cdot OA \\cdot OC}{r^2}}{\\frac{OS \\cdot OB \\cdot OD}{r^2}} = \\frac{OA \\cdot OC}{OB \\cdot OD} = \\frac{5 \\times 7}{6 \\times 8} = \\frac{35}{48}$$\n最终得解：$\\frac{OM}{ON} = \\frac{35}{48}$！",
            "svg": f"""
              {line_svg(O, M, stroke="#dc2626", stroke_w=3.0)}
              {line_svg(O, N, stroke="#2563eb", stroke_w=3.0)}
            """
        }
    ]

    html = gen_html_template(
        "例 7：外切四边形的反演与对角线中点距离之比",
        "反演后转化为平行四边形，利用相似三角形中线比求出比值 35/48",
        "08/8.md",
        view_box,
        base_svg,
        pts_svg,
        step_defs
    )
    with open("08/8/8.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open("08/8/8_steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/8 步骤提取\n\n")
        for s in step_defs:
            f.write(f"## 步骤 {s['step']}：{s['title']}\n\n{s['text']}\n\n")

    print("08/8 generated.")

build_08_8()
