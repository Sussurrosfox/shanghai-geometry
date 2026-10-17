import numpy as np
from scipy.optimize import minimize

def line_inter(p1, d1, p2, d2):
    det = d1[0]*(-d2[1]) - d1[1]*(-d2[0])
    if abs(det) < 1e-6:
        return None
    t = ((p2[0]-p1[0])*(-d2[1]) - (p2[1]-p1[1])*(-d2[0])) / det
    return p1 + t * d1

def foot(p, a, b):
    ab = b - a
    return a + np.dot(p - a, ab) / np.dot(ab, ab) * ab

def circle3(p1, p2, p3):
    d = 2 * (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))
    if abs(d) < 1e-6:
        return None, 1e9
    ux = ((p1[0]**2 + p1[1]**2)*(p2[1]-p3[1]) + (p2[0]**2 + p2[1]**2)*(p3[1]-p1[1]) + (p3[0]**2 + p3[1]**2)*(p1[1]-p2[1])) / d
    uy = ((p1[0]**2 + p1[1]**2)*(p3[0]-p2[0]) + (p2[0]**2 + p2[1]**2)*(p1[0]-p3[0]) + (p3[0]**2 + p3[1]**2)*(p2[0]-p1[0])) / d
    c = np.array([ux, uy])
    return c, np.linalg.norm(c - p1)

def angle_between(v1, v2):
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(np.clip(cos, -1.0, 1.0)))

# Parameterize by:
# P = [Px, Py], Q = [Qx, Qy]
# a1, a2 (angles from P in degrees)
# b1, b2 (angles from Q in degrees)
# Initial guess based on Match 5:
# P = (508, 78), Q = (127, 485)
# Let's inspect Match 5 parameters:
# P = [508.36, 78.68], Q = [127.14, 485.75]
# A = [387.02, 331.81] -> ang P->A: np.degrees(np.arctan2(331.81-78.68, 387.02-508.36)) = 115.58 deg
# D = [583.55, 215.40] -> ang P->D: np.degrees(np.arctan2(215.40-78.68, 583.55-508.36)) = 61.16 deg
# ang Q->A: np.degrees(np.arctan2(331.81-485.75, 387.02-127.14)) = -30.63 deg
# ang Q->B: np.degrees(np.arctan2(395.68-485.75, 356.41-127.14)) = -21.46 deg

x0 = np.array([510.0, 80.0, 130.0, 480.0, 116.0, 61.0, -31.0, -21.0])

def compute_all(params):
    Px, Py, Qx, Qy, a1, a2, b1, b2 = params
    P = np.array([Px, Py])
    Q = np.array([Qx, Qy])
    dP1 = np.array([np.cos(np.radians(a1)), np.sin(np.radians(a1))])
    dP2 = np.array([np.cos(np.radians(a2)), np.sin(np.radians(a2))])
    dQ1 = np.array([np.cos(np.radians(b1)), np.sin(np.radians(b1))])
    dQ2 = np.array([np.cos(np.radians(b2)), np.sin(np.radians(b2))])
    
    A = line_inter(P, dP1, Q, dQ1)
    B = line_inter(P, dP1, Q, dQ2)
    D = line_inter(P, dP2, Q, dQ1)
    C = line_inter(P, dP2, Q, dQ2)
    if A is None or B is None or C is None or D is None: return None
    
    O = line_inter(A, C - A, B, D - B)
    if O is None: return None
    R = foot(O, P, Q)
    E = line_inter(A, C - A, P, Q - P)
    if E is None: return None
    
    X = foot(R, A, B)
    Y = foot(R, B, C)
    Z = foot(R, C, D)
    W = foot(R, D, A)
    
    circ_c, circ_r = circle3(X, Y, Z)
    if circ_c is None: return None
    
    pts = {'P':P, 'Q':Q, 'A':A, 'B':B, 'C':C, 'D':D, 'O':O, 'R':R, 'E':E, 'X':X, 'Y':Y, 'Z':Z, 'W':W, 'CircCenter':circ_c}
    return pts, circ_r

def loss(params):
    res = compute_all(params)
    if res is None: return 1e6
    pts, circ_r = res
    key_pts = [pts['P'], pts['Q'], pts['A'], pts['B'], pts['C'], pts['D'], pts['O'], pts['R'], pts['E'], pts['X'], pts['Y'], pts['Z'], pts['W']]
    
    # Pairwise distances
    dists = []
    for i in range(len(key_pts)):
        for j in range(i+1, len(key_pts)):
            dists.append(np.linalg.norm(key_pts[i] - key_pts[j]))
    min_d = min(dists)
    
    ang_ARO = angle_between(pts['A'] - pts['R'], pts['O'] - pts['R'])
    
    arr = np.array(list(pts.values()))
    w = arr[:,0].max() - arr[:,0].min()
    h = arr[:,1].max() - arr[:,1].min()
    
    # We want:
    # min_d >= 35 (penalty if < 35)
    # ang_ARO between 20 and 35
    # w around 500-600, h around 400-500
    # circ_r around 150-220
    pen_mind = max(0, 36.0 - min_d)**2 * 100
    pen_ang = max(0, 22.0 - ang_ARO)**2 * 50 + max(0, ang_ARO - 36.0)**2 * 50
    pen_span = max(0, w - 600)**2 + max(0, h - 520)**2
    pen_r = max(0, 120 - circ_r)**2 + max(0, circ_r - 240)**2
    
    return -min_d * 2.0 - ang_ARO + pen_mind + pen_ang + pen_span * 0.1 + pen_r * 0.1

opt = minimize(loss, x0, method='Nelder-Mead', options={'maxiter': 3000})
print("Optimization finished, success:", opt.success)
res = compute_all(opt.x)
if res:
    pts, circ_r = res
    key_pts = [pts['P'], pts['Q'], pts['A'], pts['B'], pts['C'], pts['D'], pts['O'], pts['R'], pts['E'], pts['X'], pts['Y'], pts['Z'], pts['W']]
    dists = [np.linalg.norm(key_pts[i] - key_pts[j]) for i in range(len(key_pts)) for j in range(i+1, len(key_pts))]
    min_d = min(dists)
    ang_ARO = angle_between(pts['A'] - pts['R'], pts['O'] - pts['R'])
    ang_CRO = angle_between(pts['C'] - pts['R'], pts['O'] - pts['R'])
    ang_ARQ = angle_between(pts['A'] - pts['R'], pts['Q'] - pts['R'])
    ang_CRP = angle_between(pts['C'] - pts['R'], pts['P'] - pts['R'])
    
    arr = np.array(list(pts.values()))
    xmin, xmax = arr[:,0].min(), arr[:,0].max()
    ymin, ymax = arr[:,1].min(), arr[:,1].max()
    
    print(f"min_dist: {min_d:.2f}")
    print(f"ang_ARO: {ang_ARO:.2f} deg, ang_CRO: {ang_CRO:.2f} deg")
    print(f"ang_ARQ: {ang_ARQ:.2f} deg, ang_CRP: {ang_CRP:.2f} deg")
    print(f"radius: {circ_r:.2f}")
    print(f"BBox: X [{xmin:.1f}, {xmax:.1f}], Y [{ymin:.1f}, {ymax:.1f}], Size: {xmax-xmin:.1f} x {ymax-ymin:.1f}")
    print("\nCoordinates:")
    for k, v in pts.items():
        print(f"const {k:11s} = {{ x: {v[0]:.2f}, y: {v[1]:.2f} }};")
