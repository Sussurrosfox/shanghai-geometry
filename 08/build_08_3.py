import os, sys, math, json
from generate_core import *
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# 08/3 (例 2)
# ==========================================
def build_08_3():
    os.makedirs("08/3", exist_ok=True)
    A = (320.00, 110.00)
    B = (160.00, 410.00)
    C = (480.00, 410.00)
    H = (320.00, 324.67)
    O = (320.00, 302.67)
    O_prime = (320.00, 517.33)
    R_omega = 192.67
    N9 = (320.00, 313.67)
    R9 = 96.33

    # X on circle omega
    rad_x = math.radians(225)
    X = (O_prime[0] + R_omega * math.cos(rad_x), O_prime[1] + R_omega * math.sin(rad_x))
    # Y on circle Omega (homothety 1/2 from A)
    Y = ((A[0] + X[0])/2, (A[1] + X[1])/2)

    # P on circle Omega such that PX = PY (P lies on perpendicular bisector of XY)
    # Midpoint of XY
    M_xy = ((X[0] + Y[0])/2, (X[1] + Y[1])/2)
    # perp direction
    dx = Y[0] - X[0]
    dy = Y[1] - X[1]
    perp_dx = -dy
    perp_dy = dx
    l_perp = math.hypot(perp_dx, perp_dy)
    perp_dx /= l_perp
    perp_dy /= l_perp

    # Line M_xy + t * perp intersects circle Omega (N9, R9)
    # |(M_xy - N9) + t * perp|^2 = R9^2
    ox = M_xy[0] - N9[0]
    oy = M_xy[1] - N9[1]
    b_coef = 2 * (ox * perp_dx + oy * perp_dy)
    c_coef = ox*ox + oy*oy - R9*R9
    disc = b_coef*b_coef - 4*c_coef
    t = (-b_coef + math.sqrt(max(0, disc))) / 2
    P = (M_xy[0] + t * perp_dx, M_xy[1] + t * perp_dy)

    # Q = A + 2(P - A) on circle omega
    Q = (A[0] + 2*(P[0] - A[0]), A[1] + 2*(P[1] - A[1]))
    # K = X
    K = X

    view_box = "60 50 520 540"

    base_svg = f"""
      {poly_svg([A, B, C], stroke="#1e293b", stroke_w=2.0)}
      {circle_svg(N9[0], N9[1], R9, stroke="#0284c7", stroke_w=1.8)}
      {circle_svg(O_prime[0], O_prime[1], R_omega, stroke="#64748b", stroke_w=1.4, dash="4,4")}
      {line_svg(A, X, stroke="#cbd5e1", stroke_w=1.2, dash="3,3")}
      {line_svg(P, X, stroke="#e11d48", stroke_w=1.8)}
      {line_svg(P, Y, stroke="#e11d48", stroke_w=1.8)}
    """

    pts_svg = f"""
      {dot_svg(A, "#0f172a")} {label_svg(A, "A", 0, -10)}
      {dot_svg(B, "#0f172a")} {label_svg(B, "B", -16, 12)}
      {dot_svg(C, "#0f172a")} {label_svg(C, "C", 8, 12)}
      {dot_svg(H, "#64748b")} {label_svg(H, "H", 8, -4, "#64748b")}
      {dot_svg(O_prime, "#64748b")} {label_svg(O_prime, "O'", 8, 12, "#64748b")}
      {dot_svg(N9, "#0284c7")} {label_svg(N9, "N_9", 8, 4, "#0284c7")}
      {dot_svg(X, "#d97706")} {label_svg(X, "X", -16, 6, "#d97706")}
      {dot_svg(Y, "#d97706")} {label_svg(Y, "Y", -16, -6, "#d97706")}
      {dot_svg(P, "#dc2626")} {label_svg(P, "P", 8, -6, "#dc2626")}
    """

    step_defs = [
        {
            "step": 0,
            "title": "已知构型与初始条件",
            "text": "锐角 $\\bigtriangleup ABC$ 中，$H$ 为垂心，圆 $\\Omega$ 为九点圆，圆 $\\omega$ 为 $\\bigtriangleup BHC$ 外接圆（圆心 $O'$），$X$ 为圆 $\\omega$ 上一点。延长 $AX$ 与圆 $\\Omega$ 交于点 $Y$，$P$ 在圆 $\\Omega$ 上且满足 $PX = PY$。求证：$\\angle O'PX = 90^\\circ$。",
            "svg": ""
        },
        {
            "step": 1,
            "title": "① 九点圆与外接圆的外位似中心",
            "text": "设 $AB, AC, AH$ 的中点分别为 $B', C', H'$，它们均在九点圆 $\\Omega$ 上。由中点性质知 $A$ 是 $\\bigtriangleup B'C'H'$ 与 $\\bigtriangleup BCH$ 的位似中心，位似比为 $1/2$。因此 $A$ 是九点圆 $\\Omega$ 与圆 $\\omega$ 的外位似中心，位似比为 $1/2$。",
            "svg": f"""
              {line_svg(A, B, stroke="#2563eb", stroke_w=1.5, dash="3,3")}
              {line_svg(A, C, stroke="#2563eb", stroke_w=1.5, dash="3,3")}
              {line_svg(A, H, stroke="#2563eb", stroke_w=1.5, dash="3,3")}
              {dot_svg(((A[0]+B[0])/2, (A[1]+B[1])/2), "#2563eb", 3.5)}
              {dot_svg(((A[0]+C[0])/2, (A[1]+C[1])/2), "#2563eb", 3.5)}
              {dot_svg(((A[0]+H[0])/2, (A[1]+H[1])/2), "#2563eb", 3.5)}
            """
        },
        {
            "step": 2,
            "title": "② 延长位似射线交圆 $\\omega$ 于 $Q, K$",
            "text": "延长位似射线 $AP$ 与圆 $\\omega$ 交于点 $Q$，由位似性质有 $AQ = 2AP$。又 $Y$ 是 $AX$ 中点，故 $AY = \\frac{1}{2}AX$，从而 $PY \\parallel QX$ 且 $PY = \\frac{1}{2}QX$。",
            "svg": f"""
              {line_svg(A, Q, stroke="#059669", stroke_w=1.8, dash="4,4")}
              {dot_svg(Q, "#059669")} {label_svg(Q, "Q", 8, -6, "#059669")}
              {line_svg(P, Y, stroke="#e11d48", stroke_w=2.2)}
              {line_svg(Q, X, stroke="#059669", stroke_w=2.2)}
            """
        },
        {
            "step": 3,
            "title": "③ 延长 $XP$ 交圆 $\\omega$ 于 $Z$，导出等腰梯形",
            "text": "延长 $XP$ 与圆 $\\omega$ 交于点 $Z$。因为 $PX = PY$，所以 $\\angle PXY = \\angle PYX$。由平行线知 $\\angle PYX = \\angle QXK$，故圆周角相等导出弦长相等：$XZ = QK = 2PY = 2PX$！",
            "svg": f"""
              {line_svg(X, P, stroke="#dc2626", stroke_w=2.0)}
              {line_svg(P, (X[0]+2*(P[0]-X[0]), X[1]+2*(P[1]-X[1])), stroke="#dc2626", stroke_w=2.0, dash="3,3")}
              {dot_svg((X[0]+2*(P[0]-X[0]), X[1]+2*(P[1]-X[1])), "#dc2626")}
              {label_svg((X[0]+2*(P[0]-X[0]), X[1]+2*(P[1]-X[1])), "Z", 8, 6, "#dc2626")}
            """
        },
        {
            "step": 4,
            "title": "④ 垂径定理宣告 $\\angle O'PX = 90^\\circ$",
            "text": "由 $XZ = 2PX$ 知点 $P$ 恰为弦 $XZ$ 的中点！根据圆的垂径定理，连心线垂直平分非直径弦，故必有 $O'P \\bot XZ$，即 $\\angle O'PX = 90^\\circ$。证毕！",
            "svg": f"""
              {line_svg(O_prime, P, stroke="#2563eb", stroke_w=2.8)}
              {line_svg(P, X, stroke="#dc2626", stroke_w=2.8)}
              {circle_svg(P[0], P[1], 12, stroke="#2563eb", fill="rgba(37,99,235,0.1)", stroke_w=1.2)}
            """
        }
    ]

    html = gen_html_template(
        "例 2：九点圆的外位似变换与垂径定理",
        "利用三角形垂心外接圆与九点圆的外位似中心，证明连线垂直",
        "08/3.md",
        view_box,
        base_svg,
        pts_svg,
        step_defs
    )
    with open("08/3/3.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open("08/3/3_steps.md", "w", encoding="utf-8") as f:
        f.write("# 08/3 步骤提取\n\n")
        for s in step_defs:
            f.write(f"## 步骤 {s['step']}：{s['title']}\n\n{s['text']}\n\n")

    print("08/3 generated.")

build_08_3()
