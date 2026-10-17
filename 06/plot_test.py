import numpy as np
import matplotlib.pyplot as plt

pts = {
    'P': np.array([577.42, 78.08]),
    'Q': np.array([103.36, 535.00]),
    'A': np.array([430.65, 359.84]),
    'B': np.array([403.93, 411.15]),
    'C': np.array([704.10, 287.47]),
    'D': np.array([670.30, 231.60]),
    'O': np.array([511.97, 338.32]),
    'R': np.array([413.46, 236.11]),
    'E': np.array([229.97, 412.96]),
    'X': np.array([477.68, 269.56]),
    'Y': np.array([473.73, 382.38]),
    'Z': np.array([603.48, 121.15]),
    'W': np.array([468.76, 339.45]),
    'CircCenter': np.array([704.10, 333.96])
}
radius = 235.40

fig, ax = plt.subplots(figsize=(9, 7))

# Draw lines
def draw_line(p1, p2, col='gray', ls='-', lw=1.5, alpha=0.7):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=col, linestyle=ls, linewidth=lw, alpha=alpha)

# Complete quad lines:
# P-A-B
draw_line(pts['P'], pts['B'], 'blue', '-', 1.8)
# P-D-C
draw_line(pts['P'], pts['C'], 'blue', '-', 1.8)
# Q-A-D
draw_line(pts['Q'], pts['D'], 'blue', '-', 1.8)
# Q-B-C
draw_line(pts['Q'], pts['C'], 'blue', '-', 1.8)

# Diagonals:
draw_line(pts['A'], pts['C'], 'purple', '-', 1.5)
draw_line(pts['B'], pts['D'], 'purple', '-', 1.5)
# PQ and extension to E
draw_line(pts['P'], pts['Q'], 'green', '--', 1.5)
draw_line(pts['O'], pts['R'], 'red', '-', 1.5)

# Circle XYZW
theta = np.linspace(0, 2*np.pi, 200)
cx, cy = pts['CircCenter']
ax.plot(cx + radius*np.cos(theta), cy + radius*np.sin(theta), color='orange', linestyle='--', linewidth=1.5)

# Points
for name, p in pts.items():
    if name == 'CircCenter': continue
    ax.plot(p[0], p[1], 'o', color='black', markersize=5)
    ax.text(p[0]+8, p[1]-8, name, fontsize=12, fontweight='bold')

ax.set_aspect('equal')
ax.invert_yaxis() # SVG coordinate convention
plt.title("Visual inspection of complete quadrilateral setup")
plt.tight_layout()
plt.savefig("06/test_diagram.png", dpi=120)
print("Saved 06/test_diagram.png successfully!")
