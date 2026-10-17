import os, sys, math, json
from generate_core import *
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

def build_08_4():
    os.makedirs("08/4", exist_ok=True)
    O = (320.00, 270.00)
    R = 160.00

    # 4 points on circle O (optimal non-degenerate angles)
    angles = [math.radians(55), math.radians(145), math.radians(195), math.radians(245)]
    A = (O[0] + R * math.cos(angles[0]), O[1] - R * math.sin(angles[0]))
    B = (O[0] + R * math.cos(angles[1]), O[1] - R * math.sin(angles[1]))
    C = (O[0] + R * math.cos(angles[2]), O[1] - R * math.sin(angles[2]))
    D = (O[0] + R * math.cos(angles[3]), O[1] - R * math.sin(angles[3]))

    # Midpoints
    W = ((A[0]+B[0])/2, (A[1]+B[1])/2)
    X = ((B[0]+C[0])/2, (B[1]+C[1])/2)
    Y = ((C[0]+D[0])/2, (C[1]+D[1])/2)
    Z = ((D[0]+A[0])/2, (D[1]+A[1])/2)

    # Inversion: P' = O + R^2/|OP|^2 * (P - O)
    def invert(P):
        dx = P[0] - O[0]
        dy = P[1] - O[1]
        d2 = dx*dx + dy*dy
        scale = (R*R) / d2
        return (O[0] + dx * scale, O[1] + dy * scale)

    W_prime = invert(W)
    X_prime = invert(X)
    Y_prime = invert(Y)
    Z_prime = invert(Z)

    # Newton intersection point M_prime = AC \cap BD
    M_prime = line_intersect(A, C, B, D)
    # M is inversion of M_prime
    M = invert(M_prime)

    # Circumcenters of AOC, BOD, WOY, XOZ
    c_AOC, r_AOC = circumcenter(A, O, C)
    c_BOD, r_BOD = circumcenter(B, O, D)
    c_WOY, r_WOY = circumcenter(W, O, Y)
    c_XOZ, r_XOZ = circumcenter(X, O, Z)

    view_box = "60 40 520 480"

    base_svg = f"""
      {circle_svg(O[0], O[1], R, stroke="#64748b", stroke_w=1.4, dash="4,4")}
      {poly_svg([A, B, C, D], stroke="#1e293b", stroke_w=1.8)}
      {line_svg(A, C, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(B, D, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(W, Y, stroke="#94a3b8", stroke_w=1.2, dash="2,2")}
      {line_svg(X, Z, stroke="#94a3b8", stroke_w=1.2, dash="2,2")}
      {dot_svg(M, "#dc2626", 5.5)}
    """

    pts_svg = f"""
      {dot_svg(O, "#64748b")} {label_svg(O, "O", 6, -6, "#64748b")}
      {dot_svg(A, "#0f172a")} {label_svg(A, "A", 8, -6)}
      {dot_svg(B, "#0f172a")} {label_svg(B, "B", -16, -6)}
      {dot_svg(C, "#0f172a")} {label_svg(C, "C", -16, 12)}
      {dot_svg(D, "#0f172a")} {label_svg(D, "D", 8, 12)}
      {dot_svg(W, "#0284c7")} {label_svg(W, "W", -4, -10, "#0284c7")}
      {dot_svg(X, "#0284c7")} {label_svg(X, "X", -18, 4, "#0284c7")}
      {dot_svg(Y, "#0284c7")} {label_svg(Y, "Y", -4, 16, "#0284c7")}
      {dot_svg(Z, "#0284c7")} {label_svg(Z, "Z", 12, 4, "#0284c7")}
      {label_svg(M, "M", 8, -8, "#dc2626")}
    """

    step_defs = [
        {
            "step": 0,
            "title": "已知构型与待证命题",
            "text": "设四边形 $ABCD$ 内接于圆 $O$，$W, X, Y, Z$ 分别为四边中点。求证：$\\bigtriangleup AOC, \\bigtriangleup BOD, \\bigtriangleup WOY, \\bigtriangleup XOZ$ 的外接圆除了点 $O$ 之外还有一个公共点 $M$。",
            "svg": ""
        },
        {
            "step": 1,
            "title": "① 以 $O$ 为反演中心作反演变换",
            "text": "以 $O$ 为反演中心、圆 $O$ 半径 $R$ 为反演半径。圆周上的点 $A, B, C, D$ 在反演下自身不动；过反演中心 $O$ 的圆反演后均变为不过 $O$ 的直线！",
            "svg": f"""
              {circle_svg(O[0], O[1], R, stroke="#0284c7", stroke_w=2.0)}
            """
        },
        {
            "step": 2,
            "title": "② 弦中点反演为外切四边形切线交点",
            "text": "因为 $W$ 是 $AB$ 中点，故 $OW \\bot AB$。由反演定义 $OW \\cdot OW' = R^2 = OA^2$，在直角三角形中推得 $\\angle W'AO = 90^\\circ$，即 $W'A$ 与圆 $O$ 相切！同理 $X'B, Y'C, Z'D$ 均为切线，四边形 $W'X'Y'Z'$ 是圆 $O$ 的外切四边形。",
            "svg": f"""
              {poly_svg([W_prime, X_prime, Y_prime, Z_prime], stroke="#059669", stroke_w=1.6, dash="4,4")}
              {dot_svg(W_prime, "#059669")} {label_svg(W_prime, "W'", -16, -6, "#059669")}
              {dot_svg(X_prime, "#059669")} {label_svg(X_prime, "X'", -18, 12, "#059669")}
              {dot_svg(Y_prime, "#059669")} {label_svg(Y_prime, "Y'", 8, 14, "#059669")}
              {dot_svg(Z_prime, "#059669")} {label_svg(Z_prime, "Z'", 12, -6, "#059669")}
            """
        },
        {
            "step": 3,
            "title": "③ 运用牛顿定理导出四线共点 $M'$",
            "text": "根据圆外切四边形的牛顿定理，两对对角线与切点弦连线共点：对角线 $W'Y'$ 与 $X'Z'$，以及切点连线 $AC$ 与 $BD$ 这四条直线精确相交于同一点 $M'$！",
            "svg": f"""
              {line_svg(A, C, stroke="#2563eb", stroke_w=2.0)}
              {line_svg(B, D, stroke="#2563eb", stroke_w=2.0)}
              {line_svg(W_prime, Y_prime, stroke="#059669", stroke_w=2.0)}
              {line_svg(X_prime, Z_prime, stroke="#059669", stroke_w=2.0)}
              {dot_svg(M_prime, "#d97706", 5.5)}
              {label_svg(M_prime, "M'", 8, -6, "#d97706")}
            """
        },
        {
            "step": 4,
            "title": "④ 逆反演变换得出四圆共点于 $M$",
            "text": "四条直线 $AC, BD, W'Y', X'Z'$ 分别是圆 $AOC, BOD, WOY, XOZ$ 在反演下的像。因为四条直线共点于 $M'$，所以原四圆必同时通过点 $M'$ 的反演点 $M$！四圆共点得证。",
            "svg": f"""
              {circle_svg(c_AOC[0], c_AOC[1], r_AOC, stroke="#dc2626", stroke_w=1.6, opacity=0.85)}
              {circle_svg(c_BOD[0], c_BOD[1], r_BOD, stroke="#2563eb", stroke_w=1.6, opacity=0.85)}
              {circle_svg(c_WOY[0], c_WOY[1], r_WOY, stroke="#059669", stroke_w=1.6, opacity=0.85)}
              {circle_svg(c_XOZ[0], c_XOZ[1], r_XOZ, stroke="#d97706", stroke_w=1.6, opacity=0.85)}
              {dot_svg(M, "#dc2626", 6)}
              {label_svg(M, "M (四圆第二交点)", 10, -8, "#dc2626")}
            """
        }
    ]

    html = gen_html_template(
        "例 3：圆内接四边形的中点反演与四圆共点",
        "以圆心为中心作反演变换，将中点圆转化为外切四边形牛顿定理共点线",
        "08/4.md",
        view_box,
        base_svg,
        pts_svg,
        step_defs
    )
    with open("08/4/4.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open("08/4/4_steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/4 步骤提取\n\n")
        for s in step_defs:
            f.write(f"## 步骤 {s['step']}：{s['title']}\n\n{s['text']}\n\n")

    # 写入 08/4/steps.md
    with open("08/4/steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/4（例 3）平面几何证明分步规划\n\n## 题目概要\n四边形 $ABCD$ 内接于圆 $O$，$W, X, Y, Z$ 分别为 $AB, BC, CD, DA$ 中点。证明：$\\bigtriangleup AOC, \\bigtriangleup BOD, \\bigtriangleup WOY, \\bigtriangleup XOZ$ 的外接圆除了点 $O$ 之外还有一个公共点。\n\n## 证明规划设计\n- Step 0：初始已知构型与圆内接四边形。\n- Step 1：以 $O$ 为中心作反演变换。\n- Step 2：各边中点反演为外切四边形切线交点。\n- Step 3：牛顿定理导出 $AC, BD, W'Y', X'Z'$ 四线共点于 $M'$。\n- Step 4：逆反演导出四圆共点于 $M$。\n")

    print("08/4 generated.")

build_08_4()
