import numpy as np

def line_inter_2pts(p1, p2, p3, p4):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(denom) < 1e-6: return None
    px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / denom
    return np.array([px, py])

def foot(p, a, b):
    ab = b - a
    return a + np.dot(p - a, ab) / np.dot(ab, ab) * ab

def circle3(p1, p2, p3):
    d = 2 * (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))
    if abs(d) < 1e-6: return None, 1e9
    ux = ((p1[0]**2 + p1[1]**2)*(p2[1]-p3[1]) + (p2[0]**2 + p2[1]**2)*(p3[1]-p1[1]) + (p3[0]**2 + p3[1]**2)*(p1[1]-p2[1])) / d
    uy = ((p1[0]**2 + p1[1]**2)*(p3[0]-p2[0]) + (p2[0]**2 + p2[1]**2)*(p1[0]-p3[0]) + (p3[0]**2 + p3[1]**2)*(p2[0]-p1[0])) / d
    c = np.array([ux, uy])
    return c, np.linalg.norm(c - p1)

def angle_between(v1, v2):
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(np.clip(cos, -1.0, 1.0)))

# In Match 5, P was (508, 78), Q was (127, 485)
# Let's explore systematically around this topology:
# P at top-right, Q at bottom-left
# Line PAB and PDC go downwards-left
# Line QAD and QBC go upwards-right

candidates = []

for Px in np.linspace(480, 560, 9):
    for Py in np.linspace(60, 100, 5):
        P = np.array([Px, Py])
        for Qx in np.linspace(100, 160, 7):
            for Qy in np.linspace(460, 520, 5):
                Q = np.array([Qx, Qy])
                
                for angP1 in np.linspace(110, 130, 9): # L_PAB
                    for angP2 in np.linspace(65, 85, 9):  # L_PDC
                        dP1 = np.array([np.cos(np.radians(angP1)), np.sin(np.radians(angP1))])
                        dP2 = np.array([np.cos(np.radians(angP2)), np.sin(np.radians(angP2))])
                        
                        for angQ1 in np.linspace(-35, -15, 9): # L_QAD
                            for angQ2 in np.linspace(-65, -45, 9): # L_QBC
                                dQ1 = np.array([np.cos(np.radians(angQ1)), np.sin(np.radians(angQ1))])
                                dQ2 = np.array([np.cos(np.radians(angQ2)), np.sin(np.radians(angQ2))])
                                
                                A = line_inter_2pts(P, P+dP1, Q, Q+dQ1)
                                B = line_inter_2pts(P, P+dP1, Q, Q+dQ2)
                                D = line_inter_2pts(P, P+dP2, Q, Q+dQ1)
                                C = line_inter_2pts(P, P+dP2, Q, Q+dQ2)
                                
                                if A is None or B is None or C is None or D is None: continue
                                
                                # Check orders
                                if not (np.linalg.norm(B-P) > np.linalg.norm(A-P) + 40): continue
                                if not (np.linalg.norm(C-P) > np.linalg.norm(D-P) + 40): continue
                                if not (np.linalg.norm(D-Q) > np.linalg.norm(A-Q) + 40): continue
                                if not (np.linalg.norm(C-Q) > np.linalg.norm(B-Q) + 40): continue
                                
                                O = line_inter_2pts(A, C, B, D)
                                if O is None: continue
                                R = foot(O, P, Q)
                                E = line_inter_2pts(A, C, P, Q)
                                if E is None: continue
                                
                                ang_ARO = angle_between(A - R, O - R)
                                if ang_ARO < 18 or ang_ARO > 38: continue
                                
                                X = foot(R, A, B)
                                Y = foot(R, B, C)
                                Z = foot(R, C, D)
                                W = foot(R, D, A)
                                
                                c_circ, r_circ = circle3(X, Y, Z)
                                if c_circ is None or r_circ < 80 or r_circ > 220: continue
                                if abs(np.linalg.norm(c_circ - W) - r_circ) > 1e-3: continue
                                
                                all_dict = {'P':P, 'Q':Q, 'A':A, 'B':B, 'C':C, 'D':D, 'O':O, 'R':R, 'E':E, 'X':X, 'Y':Y, 'Z':Z, 'W':W, 'CircCenter':c_circ}
                                key_pts = [P, Q, A, B, C, D, O, R, E, X, Y, Z, W]
                                min_d = min(np.linalg.norm(key_pts[i] - key_pts[j]) for i in range(len(key_pts)) for j in range(i+1, len(key_pts)))
                                if min_d < 30: continue
                                
                                arr = np.array(list(all_dict.values()))
                                xmin, xmax = arr[:,0].min(), arr[:,0].max()
                                ymin, ymax = arr[:,1].min(), arr[:,1].max()
                                w, h = xmax - xmin, ymax - ymin
                                if w > 650 or h > 550: continue
                                
                                score = min_d * 2.0 + ang_ARO
                                candidates.append((score, min_d, ang_ARO, r_circ, all_dict, (xmin, ymin, w, h)))

print(f"Candidates found: {len(candidates)}")
if candidates:
    candidates.sort(key=lambda c: -c[0])
    best = candidates[0]
    print(f"Top Score: {best[0]:.2f}, min_d: {best[1]:.2f}, ang_ARO: {best[2]:.2f} deg, radius: {best[3]:.2f}")
    xmin, ymin, w, h = best[5]
    print(f"Box: [{xmin:.1f}, {ymin:.1f}] -> [{xmin+w:.1f}, {ymin+h:.1f}], span {w:.1f}x{h:.1f}")
    for k, v in best[4].items():
        print(f"  const {k:11s} = {{ x: {v[0]:.2f}, y: {v[1]:.2f} }};")
