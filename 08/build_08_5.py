import os, sys, math, json
from generate_core import *
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

def build_08_5():
    os.makedirs("08/5", exist_ok=True)
    O = (320.00, 260.00)
    r = 85.00

    t_E = math.radians(40)
    t_F = math.radians(125)
    t_G = math.radians(210)
    t_H = math.radians(305)

    def get_tangent_pt(t):
        return (O[0] + r*math.cos(t), O[1] - r*math.sin(t))

    E = get_tangent_pt(t_E)
    F = get_tangent_pt(t_F)
    G = get_tangent_pt(t_G)
    H = get_tangent_pt(t_H)

    def tangent_line_pts(t):
        pt = get_tangent_pt(t)
        v = (-math.sin(t), -math.cos(t))
        return pt, (pt[0] + 100*v[0], pt[1] + 100*v[1])

    pE1, pE2 = tangent_line_pts(t_E)
    pF1, pF2 = tangent_line_pts(t_F)
    pG1, pG2 = tangent_line_pts(t_G)
    pH1, pH2 = tangent_line_pts(t_H)

    B = line_intersect(pE1, pE2, pF1, pF2)
    C = line_intersect(pF1, pF2, pG1, pG2)
    D = line_intersect(pG1, pG2, pH1, pH2)
    A = line_intersect(pH1, pH2, pE1, pE2)

    P = line_intersect(A, C, B, D)
    Q = line_intersect(G, H, F, E)
    R_pt = line_intersect(H, E, G, F)

    # Foot of O on BD
    v_BD = (D[0] - B[0], D[1] - B[1])
    l_BD = math.hypot(*v_BD)
    u_BD = (v_BD[0]/l_BD, v_BD[1]/l_BD)
    dot = (O[0] - B[0])*u_BD[0] + (O[1] - B[1])*u_BD[1]
    M = (B[0] + dot*u_BD[0], B[1] + dot*u_BD[1])

    view_box = "120 70 420 400"

    base_svg = f"""
      {circle_svg(O[0], O[1], r, stroke="#0284c7", stroke_w=1.6)}
      {poly_svg([A, B, C, D], stroke="#1e293b", stroke_w=1.8)}
      {line_svg(A, C, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(B, D, stroke="#2563eb", stroke_w=1.8)}
      {line_svg(E, G, stroke="#94a3b8", stroke_w=1.0, dash="2,2")}
      {line_svg(F, H, stroke="#94a3b8", stroke_w=1.0, dash="2,2")}
    """

    pts_svg = f"""
      {dot_svg(O, "#0284c7")} {label_svg(O, "O", 6, -6, "#0284c7")}
      {dot_svg(A, "#0f172a")} {label_svg(A, "A", 8, -4)}
      {dot_svg(B, "#0f172a")} {label_svg(B, "B", -8, -10)}
      {dot_svg(C, "#0f172a")} {label_svg(C, "C", -16, 8)}
      {dot_svg(D, "#0f172a")} {label_svg(D, "D", 8, 12)}
      {dot_svg(E, "#0284c7", 3.5)} {label_svg(E, "E", 6, -6, "#0284c7")}
      {dot_svg(F, "#0284c7", 3.5)} {label_svg(F, "F", -14, -6, "#0284c7")}
      {dot_svg(G, "#0284c7", 3.5)} {label_svg(G, "G", -14, 8, "#0284c7")}
      {dot_svg(H, "#0284c7", 3.5)} {label_svg(H, "H", 6, 8, "#0284c7")}
      {dot_svg(P, "#d97706", 4.5)} {label_svg(P, "P", 8, 8, "#d97706")}
      {dot_svg(M, "#dc2626", 5.5)} {label_svg(M, "M", -16, -6, "#dc2626")}
    """

    step_defs = [
        {
            "step": 0,
            "title": "已知构型与初始条件",
            "text": "设四边形 $ABCD$ 的内切圆为圆 $O$，过 $O$ 作 $OM \\bot BD$ 于点 $M$。求证：$BD$ 平分 $\\angle AMC$。",
            "svg": f"""
              {line_svg(O, M, stroke="#dc2626", stroke_w=1.8, dash="3,3")}
              {line_svg(M, A, stroke="#e11d48", stroke_w=1.8)}
              {line_svg(M, C, stroke="#e11d48", stroke_w=1.8)}
            """
        },
        {
            "step": 1,
            "title": "① 切点弦与对角线共点 $P$",
            "text": "设圆 $O$ 与四边分别相切于点 $E, F, G, H$。根据圆外切四边形的牛顿定理，两对角线 $AC$ 与 $BD$ 的交点 $P$，必同时落在两切点弦 $EG$ 与 $FH$ 上，即四线共点于 $P$。",
            "svg": f"""
              {line_svg(E, G, stroke="#d97706", stroke_w=2.0)}
              {line_svg(F, H, stroke="#d97706", stroke_w=2.0)}
              {dot_svg(P, "#d97706", 6)}
            """
        },
        {
            "step": 2,
            "title": "② 切点弦交点 $Q$ 的极线为 $BD$",
            "text": "设 $GH$ 与 $FE$ 的延长线交于点 $Q$。因为 $EF$ 为点 $B$ 关于圆 $O$ 的极线，点 $Q$ 在 $EF$ 上，由配极原则 $Q$ 的极线过点 $B$；同理 $Q$ 的极线过点 $D$。因此直线 $BD$ 恰为点 $Q$ 关于圆 $O$ 的极线！",
            "svg": f"""
              {line_svg(G, Q, stroke="#059669", stroke_w=1.5, dash="3,3")}
              {line_svg(F, Q, stroke="#059669", stroke_w=1.5, dash="3,3")}
              {dot_svg(Q, "#059669", 5.5)} {label_svg(Q, "Q", 8, -6, "#059669")}
              {line_svg(B, D, stroke="#059669", stroke_w=2.5)}
            """
        },
        {
            "step": 3,
            "title": "③ 极线垂直定理导出 $Q, M, O$ 共线",
            "text": "由极点与极线垂直定理，极点 $Q$ 与圆心 $O$ 的连线必垂直于其极线 $BD$，即 $QO \\bot BD$。又已知 $OM \\bot BD$，由过同一点垂直于同一直线的垂线唯一性，必有 $Q, M, O$ 三点共线，故 $QM \\bot BD$！",
            "svg": f"""
              {line_svg(Q, O, stroke="#dc2626", stroke_w=2.0)}
              {line_svg(O, M, stroke="#dc2626", stroke_w=2.0)}
              {dot_svg(M, "#dc2626", 6)}
            """
        },
        {
            "step": 4,
            "title": "④ 调和点列 $(Q, P; A, C)$ 导出角平分线",
            "text": "由完全四边形完全共轭性质，割线截出的点列 $(Q, P; A, C)$ 是调和点列。以 $M$ 为顶点引出线束 $(MQ, MP; MA, MC)$，它是一组调和线束。因为两共轭射线 $MQ \\bot MP$（即 $MQ \\bot BD$），互相垂直的调和共轭射线必平分另外两射线的夹角！故直线 $MP$（即 $BD$）平分 $\\angle AMC$。证毕！",
            "svg": f"""
              {line_svg(M, A, stroke="#e11d48", stroke_w=2.5)}
              {line_svg(M, C, stroke="#e11d48", stroke_w=2.5)}
              {line_svg(M, Q, stroke="#dc2626", stroke_w=2.0, dash="3,3")}
              {line_svg(M, P, stroke="#2563eb", stroke_w=2.8)}
            """
        }
    ]

    html = gen_html_template(
        "例 4：外切四边形的极线理论与调和角平分线",
        "利用配极原则证明直线为极线，再由互相垂直的调和线束导出角平分线",
        "08/5.md",
        view_box,
        base_svg,
        pts_svg,
        step_defs
    )
    with open("08/5/5.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open("08/5/5_steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/5 步骤提取\n\n")
        for s in step_defs:
            f.write(f"## 步骤 {s['step']}：{s['title']}\n\n{s['text']}\n\n")

    with open("08/5/steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/5（例 4）平面几何证明分步规划\n\n## 题目概要\n设四边形 $ABCD$ 的内切圆为圆 $O$，过 $O$ 作 $OM \\bot BD$。求证：$BD$ 平分 $\\angle AMC$。\n\n## 证明规划设计\n- Step 0：初始已知构型与圆内切四边形及垂线 $OM$。\n- Step 1：牛顿定理导出对角线与切点弦共点于 $P$。\n- Step 2：配极原则导出直线 $BD$ 是交点 $Q$ 的极线。\n- Step 3：连心线垂直极线导出 $Q, M, O$ 三点共线且 $QM \\bot BD$。\n- Step 4：调和点列 $(Q, P; A, C)$ 结合 $QM \\bot MP$ 导出 $BD$ 平分 $\\angle AMC$。\n")

    print("08/5 generated.")

build_08_5()
