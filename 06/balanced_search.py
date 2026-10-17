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

# Let's search around this balanced layout
# Let A, B, C, D be defined such that AB and CD meet at P (above),
# AD and BC meet at Q (left).
# For example:
# Let P = (400, 60), Q = (80, 420)
# A is on line PA, B is on line PB (PA=PB is line 1, wait, P, A, B collinear)
# So line 1 is through P: P + t * dP1 (contains A and B)
# line 2 is through P: P + t * dP2 (contains D and C)
# line 3 is through Q: Q + s * dQ1 (contains A and D)
# line 4 is through Q: Q + s * dQ2 (contains B and C)

candidates = []

for Px in np.linspace(350, 450, 6):
    for Py in np.linspace(50, 80, 4):
        P = np.array([Px, Py])
        for Qx in np.linspace(60, 120, 5):
            for Qy in np.linspace(380, 440, 4):
                Q = np.array([Qx, Qy])
                
                # Lines from P:
                # L1 (P-A-B) points downwards-left (angle around 125 to 145 deg)
                # L2 (P-D-C) points downwards-right (angle around 65 to 85 deg)
                for a1 in np.linspace(125, 145, 6):
                    for a2 in np.linspace(65, 85, 6):
                        dP1 = np.array([np.cos(np.radians(a1)), np.sin(np.radians(a1))])
                        dP2 = np.array([np.cos(np.radians(a2)), np.sin(np.radians(a2))])
                        
                        # Lines from Q:
                        # L3 (Q-A-D) points upwards-right (angle around -50 to -25 deg)
                        # L4 (Q-B-C) points rightwards (angle around -15 to 15 deg)
                        for b1 in np.linspace(-50, -25, 6):
                            for b2 in np.linspace(-15, 15, 6):
                                dQ1 = np.array([np.cos(np.radians(b1)), np.sin(np.radians(b1))])
                                dQ2 = np.array([np.cos(np.radians(b2)), np.sin(np.radians(b2))])
                                
                                A = line_inter_2pts(P, P+dP1, Q, Q+dQ1)
                                B = line_inter_2pts(P, P+dP1, Q, Q+dQ2)
                                D = line_inter_2pts(P, P+dP2, Q, Q+dQ1)
                                C = line_inter_2pts(P, P+dP2, Q, Q+dQ2)
                                
                                if A is None or B is None or C is None or D is None: continue
                                
                                # Check orders
                                lAB = np.linalg.norm(B - A)
                                lCD = np.linalg.norm(C - D)
                                lAD = np.linalg.norm(D - A)
                                lBC = np.linalg.norm(C - B)
                                
                                if not (np.dot(B-A, dP1) > 0 and np.dot(C-D, dP2) > 0): continue
                                if not (np.dot(D-A, dQ1) > 0 and np.dot(C-B, dQ2) > 0): continue
                                
                                # Balanced edge lengths! (80 to 260)
                                if lAB < 70 or lAB > 250: continue
                                if lCD < 70 or lCD > 250: continue
                                if lAD < 100 or lAD > 280: continue
                                if lBC < 120 or lBC > 300: continue
                                
                                O = line_inter_2pts(A, C, B, D)
                                if O is None: continue
                                R = foot(O, P, Q)
                                E = line_inter_2pts(A, C, P, Q)
                                if E is None: continue
                                
                                ang_ARO = angle_between(A - R, O - R)
                                if ang_ARO < 10 or ang_ARO > 40: continue
                                
                                X = foot(R, A, B)
                                Y = foot(R, B, C)
                                Z = foot(R, C, D)
                                W = foot(R, D, A)
                                
                                c_circ, r_circ = circle3(X, Y, Z)
                                if c_circ is None or r_circ < 80 or r_circ > 300: continue
                                err_W = abs(np.linalg.norm(c_circ - W) - r_circ)
                                if err_W > 1e-3: continue
                                
                                all_dict = {'P':P, 'Q':Q, 'A':A, 'B':B, 'C':C, 'D':D, 'O':O, 'R':R, 'E':E, 'X':X, 'Y':Y, 'Z':Z, 'W':W, 'CircCenter':c_circ}
                                key_pts = [P, Q, A, B, C, D, O, R, E, X, Y, Z, W]
                                min_d = min(np.linalg.norm(key_pts[i] - key_pts[j]) for i in range(len(key_pts)) for j in range(i+1, len(key_pts)))
                                if min_d < 22: continue
                                
                                arr = np.array(list(all_dict.values()))
                                xmin, xmax = arr[:,0].min(), arr[:,0].max()
                                ymin, ymax = arr[:,1].min(), arr[:,1].max()
                                w, h = xmax - xmin, ymax - ymin
                                if w > 720 or h > 600: continue
                                
                                score = min_d * 2.0 + ang_ARO - abs(r_circ - 180) * 0.1
                                candidates.append((score, min_d, ang_ARO, r_circ, all_dict, (xmin, ymin, w, h), (lAB, lBC, lCD, lAD)))

print(f"Total candidates found: {len(candidates)}")
if candidates:
    candidates.sort(key=lambda c: -c[0])
    best = candidates[0]
    print(f"Top Score: {best[0]:.2f}, min_d: {best[1]:.2f}, ang_ARO: {best[2]:.2f} deg, radius: {best[3]:.2f}")
    print(f"Edges: AB={best[6][0]:.1f}, BC={best[6][1]:.1f}, CD={best[6][2]:.1f}, DA={best[6][3]:.1f}")
    xmin, ymin, w, h = best[5]
    print(f"Box: [{xmin:.1f}, {ymin:.1f}] -> [{xmin+w:.1f}, {ymin+h:.1f}], span {w:.1f}x{h:.1f}")
    for k, v in best[4].items():
        print(f"  const {k:11s} = {{ x: {v[0]:.2f}, y: {v[1]:.2f} }};")
