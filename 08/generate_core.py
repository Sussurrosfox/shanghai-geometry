import os, sys, math, json
from template_builder import gen_html_template

sys.stdout.reconfigure(encoding='utf-8')

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def pt(p):
    return f"{p[0]:.2f},{p[1]:.2f}"

def circle_svg(cx, cy, r, stroke="#2563eb", fill="none", stroke_w=1.5, dash=None, opacity=1.0):
    d_attr = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" stroke="{stroke}" fill="{fill}" stroke-width="{stroke_w}" opacity="{opacity}"{d_attr}/>'

def line_svg(p1, p2, stroke="#2563eb", stroke_w=1.5, dash=None, opacity=1.0, marker=None):
    d_attr = f' stroke-dasharray="{dash}"' if dash else ''
    m_attr = f' marker-end="url(#{marker})"' if marker else ''
    return f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" stroke="{stroke}" stroke-width="{stroke_w}" opacity="{opacity}"{d_attr}{m_attr}/>'

def poly_svg(pts, stroke="#2563eb", fill="none", stroke_w=1.5, opacity=1.0, dash=None):
    p_str = " ".join([f"{p[0]:.2f},{p[1]:.2f}" for p in pts])
    d_attr = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{p_str}" stroke="{stroke}" fill="{fill}" stroke-width="{stroke_w}" opacity="{opacity}"{d_attr}/>'

def dot_svg(p, color="#2563eb", r=4):
    return f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{r}" fill="{color}"/>'

def label_svg(p, text, dx=8, dy=-8, color="#0f172a", font_size=13):
    return f'<text x="{p[0]+dx:.2f}" y="{p[1]+dy:.2f}" fill="{color}" font-size="{font_size}" font-weight="600" stroke="#ffffff" stroke-width="4px" paint-order="stroke fill">{text}</text>'

def circumcenter(A, B, C):
    ax, ay = A
    bx, by = B
    cx, cy = C
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax*ax + ay*ay)*(by - cy) + (bx*bx + by*by)*(cy - ay) + (cx*cx + cy*cy)*(ay - by)) / d
    uy = ((ax*ax + ay*ay)*(cx - bx) + (bx*bx + by*by)*(ax - cx) + (cx*cx + cy*cy)*(bx - ax)) / d
    return (ux, uy), math.hypot(ux - ax, uy - ay)

def line_intersect(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if abs(denom) < 1e-9: return None
    t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denom
    return (x1 + t*(x2 - x1), y1 + t*(y2 - y1))

print("Helper functions ready.")
