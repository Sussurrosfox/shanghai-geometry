import os, sys, math, json
from generate_core import *
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

def build_08_6():
    os.makedirs("08/6", exist_ok=True)
    A = (320.00, 110.00)
    B = (130.00, 410.00)
    C = (570.00, 410.00)
    O = (350.00, 339.17)
    R = 231.12
    E = (350.00, 570.29)
    I = (332.30, 298.67)
    Ia = (367.70, 841.91)
    D = (284.00, 410.00)
    I1 = (233.48, 353.05)
    I2 = (382.82, 322.33)
    O1 = (219.82, 211.26)
    r1 = 142.44
    O2 = (409.84, 198.88)
    r2 = 126.37
    M = (120.34, 313.22)
    N = (536.17, 202.20)
    X = (367.70, 410.00)
    P0 = (315.84, 261.02)

    view_box = "40 40 600 560"

    base_svg = f"""
      {poly_svg([A, B, C], stroke="#1e293b", stroke_w=2.0)}
      {circle_svg(O[0], O[1], R, stroke="#64748b", stroke_w=1.4, dash="4,4")}
      {circle_svg(O1[0], O1[1], r1, stroke="#0284c7", stroke_w=1.2, dash="3,3", opacity=0.7)}
      {circle_svg(O2[0], O2[1], r2, stroke="#059669", stroke_w=1.2, dash="3,3", opacity=0.7)}
      {line_svg(M, N, stroke="#e11d48", stroke_w=2.0)}
      {dot_svg(P0, "#dc2626", 5.5)}
    """

    pts_svg = f"""
      {dot_svg(A, "#0f172a")} {label_svg(A, "A", 0, -10)}
      {dot_svg(B, "#0f172a")} {label_svg(B, "B", -16, 12)}
      {dot_svg(C, "#0f172a")} {label_svg(C, "C", 8, 12)}
      {dot_svg(D, "#d97706")} {label_svg(D, "D", 0, 16, "#d97706")}
      {dot_svg(I, "#0284c7")} {label_svg(I, "I", 8, -4, "#0284c7")}
      {dot_svg(I1, "#0284c7", 3.5)} {label_svg(I1, "I_1", -16, 4, "#0284c7")}
      {dot_svg(I2, "#059669", 3.5)} {label_svg(I2, "I_2", 8, 4, "#059669")}
      {dot_svg(M, "#e11d48")} {label_svg(M, "M", -16, -6, "#e11d48")}
      {dot_svg(N, "#e11d48")} {label_svg(N, "N", 10, -6, "#e11d48")}
      {label_svg(P0, "P_0 (定点)", 10, -6, "#dc2626")}
    """

    step_defs = [
        {
            "step": 0,
            "title": "已知条件与构型引入",
            "text": "给定 $\\bigtriangleup ABC$，点 $D$ 为边 $BC$ 上的动点，$\\bigtriangleup ABC, \\bigtriangleup ABD, \\bigtriangleup ACD$ 的内心分别为 $I, I_1, I_2$。圆 $IAI_1, IAI_2$ 与外接圆分别交于异于 $A$ 的点 $M, N$。求证：直线 $MN$ 恒过一个定点 $P_0$。",
            "svg": ""
        },
        {
            "step": 1,
            "title": "① 引入弧中点 $E$ 与鸡爪定理反演对偶",
            "text": "设外接圆弧 $BC$ 的中点为 $E$。由鸡爪定理知 $EB = EC = EI = EI_a$，其中 $I_a$ 为 $\\bigtriangleup ABC$ 的 $A$-旁心。由此导出核心反演对偶式：$AI \\cdot AI_a = AB \\cdot AC$。在以 $A$ 为中心、$\\sqrt{AB \\cdot AC}$ 为半径的反演下，内心 $I$ 的反演像恰为旁心 $I_a$。",
            "svg": f"""
              {line_svg(A, (A[0]+1.5*(I[0]-A[0]), A[1]+1.5*(I[1]-A[1])), stroke="#2563eb", stroke_w=1.5, dash="3,3")}
              {dot_svg(E, "#059669")} {label_svg(E, "E", 8, 12, "#059669")}
            """
        },
        {
            "step": 2,
            "title": "② 圆周角导出两圆在 $A$ 点严格正交",
            "text": "在 $\\bigtriangleup ABD$ 与 $\\bigtriangleup ACD$ 中由内角平分线推导圆周角：$\\angle O_1 A I = 90^\\circ - \\frac{1}{2}\\angle ADB$，$\\angle O_2 A I = 90^\\circ - \\frac{1}{2}\\angle ADC$。两角相加得到：$\\angle O_1 A O_2 = \\frac{1}{2}(\\angle ADB + \\angle ADC) = 90^\\circ$！故两圆在公共点 $A$ 处严格互相垂直正交。",
            "svg": f"""
              {line_svg(A, O1, stroke="#0284c7", stroke_w=1.8)}
              {line_svg(A, O2, stroke="#059669", stroke_w=1.8)}
              {dot_svg(O1, "#0284c7")} {label_svg(O1, "O_1", -16, -6, "#0284c7")}
              {dot_svg(O2, "#059669")} {label_svg(O2, "O_2", 8, -6, "#059669")}
            """
        },
        {
            "step": 3,
            "title": "③ 等角共轭反演将圆转化为垂直直线",
            "text": "以 $A$ 为中心、$\\sqrt{AB \\cdot AC}$ 为半径作等角共轭反演：外接圆反演为直线 $BC$；圆 $IAI_1$ 与 $IAI_2$ 分别反演为过 $I_a$ 的两条直线 $I_a M'$ 与 $I_a N'$。正交性保证 $\\angle M' I_a N' = 90^\\circ$ 严格为直角！",
            "svg": f"""
              {line_svg(B, C, stroke="#2563eb", stroke_w=2.5)}
            """
        },
        {
            "step": 4,
            "title": "④ 射影定理导出共轴圆系恒过定点 $Y$",
            "text": "设 $I_a$ 到直线 $BC$ 的垂足为 $X$（即切点），$X$ 是与动点 $D$ 完全无关的定点。在直角三角形 $\\bigtriangleup M' I_a N'$ 中由射影定理：$XM' \\cdot XN' = -XI_a^2 = -r_a^2$。故圆系 $\\odot(AM'N')$ 为共轴圆系，且直线 $AX$ 与该圆系的第二交点 $Y$ 为定点！",
            "svg": f"""
              {line_svg(A, X, stroke="#94a3b8", stroke_w=1.5, dash="3,3")}
              {dot_svg(X, "#64748b")} {label_svg(X, "X", 8, 12, "#64748b")}
            """
        },
        {
            "step": 5,
            "title": "⑤ 逆反演导出直线 $MN$ 恒过定点 $P_0$",
            "text": "逆反演变换下，过定点 $Y$ 的圆 $\\odot(AM'N')$ 必反演为过定点 $P_0 = \\mathcal{I}^*(Y)$ 的直线 $MN$！因为 $Y$ 与动点 $D$ 完全无关，所以点 $P_0$ 是一个完全固定的定点，直线 $MN$ 恒过定点 $P_0$。原命题得证！",
            "svg": f"""
              {line_svg(M, N, stroke="#e11d48", stroke_w=2.8)}
              {dot_svg(P0, "#dc2626", 6.5)}
              {circle_svg(P0[0], P0[1], 12, stroke="#dc2626", fill="rgba(220,38,38,0.15)", stroke_w=1.5)}
            """
        }
    ]

    html = gen_html_template(
        "例 5：动点内心的等角共轭反演与定点直线",
        "利用等角共轭反演与射影定理证明共轴圆系，导出直线过定点",
        "08/6.md",
        view_box,
        base_svg,
        pts_svg,
        step_defs
    )
    with open("08/6/6.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open("08/6/6_steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/6 步骤提取\n\n")
        for s in step_defs:
            f.write(f"## 步骤 {s['step']}：{s['title']}\n\n{s['text']}\n\n")

    print("08/6 generated.")

build_08_6()
