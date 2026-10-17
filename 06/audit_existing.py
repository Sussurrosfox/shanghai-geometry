import numpy as np

A = np.array([180.00, 340.00])
B = np.array([280.00, 220.00])
C = np.array([380.00, 280.00])
D = np.array([360.00, 380.00])
O = np.array([319.15, 298.30])
P = np.array([427.37, 43.16])
Q = np.array([656.47, 445.88])
R = np.array([510.51, 189.37])
E = np.array([535.56, 233.33])
X = np.array([389.58, 88.50])
Y = np.array([436.04, 313.62])
Z = np.array([402.49, 167.57])
W = np.array([463.09, 403.02])

print("AUDIT EXISTING COORDS IN 06/4/4.html:")

# 1. P is intersection of AB and CD?
# Line AB: A=(180, 340), B=(280, 220)
# Vector AB = (100, -120). Vector AP = (247.37, -296.84).
cross_PAB = (B[0]-A[0])*(P[1]-A[1]) - (B[1]-A[1])*(P[0]-A[0])
print(f"Collinear P, A, B: cross = {cross_PAB:.4f}")
# Line CD: C=(380, 280), D=(360, 380).
cross_PCD = (D[0]-C[0])*(P[1]-C[1]) - (D[1]-C[1])*(P[0]-C[0])
print(f"Collinear P, C, D: cross = {cross_PCD:.4f}")

# 2. Q is intersection of AD and BC?
# Line AD: A=(180, 340), D=(360, 380)
cross_QAD = (D[0]-A[0])*(Q[1]-A[1]) - (D[1]-A[1])*(Q[0]-A[0])
print(f"Collinear Q, A, D: cross = {cross_QAD:.4f}")
# Line BC: B=(280, 220), C=(380, 280)
cross_QBC = (C[0]-B[0])*(Q[1]-B[1]) - (C[1]-B[1])*(Q[0]-B[0])
print(f"Collinear Q, B, C: cross = {cross_QBC:.4f}")

# 3. O is AC intersect BD?
cross_ACO = (C[0]-A[0])*(O[1]-A[1]) - (C[1]-A[1])*(O[0]-A[0])
cross_BDO = (D[0]-B[0])*(O[1]-B[1]) - (D[1]-B[1])*(O[0]-B[0])
print(f"O on AC cross: {cross_ACO:.4f}, O on BD cross: {cross_BDO:.4f}")

# 4. OR perp PQ?
vPQ = Q - P
vOR = R - O
print(f"OR perp PQ dot: {np.dot(vOR, vPQ):.4f}")
print(f"R on PQ cross: {(Q[0]-P[0])*(R[1]-P[1]) - (Q[1]-P[1])*(R[0]-P[0]):.4f}")

# 5. Feet X, Y, Z, W from R to AB, BC, CD, DA:
# X on AB:
print(f"RX dot AB: {np.dot(X-R, B-A):.4f}")
print(f"X on AB cross: {(B[0]-A[0])*(X[1]-A[1]) - (B[1]-A[1])*(X[0]-A[0]):.4f}")

# Y on BC:
print(f"RY dot BC: {np.dot(Y-R, C-B):.4f}")
print(f"Y on BC cross: {(C[0]-B[0])*(Y[1]-B[1]) - (C[1]-B[1])*(Y[0]-B[0]):.4f}")

# Z on CD:
print(f"RZ dot CD: {np.dot(Z-R, D-C):.4f}")
print(f"Z on CD cross: {(D[0]-C[0])*(Z[1]-C[1]) - (D[1]-C[1])*(Z[0]-C[0]):.4f}")

# W on DA:
print(f"RW dot DA: {np.dot(W-R, D-A):.4f}")
print(f"W on DA cross: {(D[0]-A[0])*(W[1]-A[1]) - (D[1]-A[1])*(W[0]-A[0]):.4f}")

# 6. Circle XYZW
def circle3(p1, p2, p3):
    d = 2 * (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))
    ux = ((p1[0]**2 + p1[1]**2)*(p2[1]-p3[1]) + (p2[0]**2 + p2[1]**2)*(p3[1]-p1[1]) + (p3[0]**2 + p3[1]**2)*(p1[1]-p2[1])) / d
    uy = ((p1[0]**2 + p1[1]**2)*(p3[0]-p2[0]) + (p2[0]**2 + p2[1]**2)*(p1[0]-p3[0]) + (p3[0]**2 + p3[1]**2)*(p2[0]-p1[0])) / d
    c = np.array([ux, uy])
    return c, np.linalg.norm(c - p1)

c, r = circle3(X, Y, Z)
print(f"Circle center: {c}, radius: {r:.4f}")
print(f"Dist center to X: {np.linalg.norm(c - X):.4f}")
print(f"Dist center to Y: {np.linalg.norm(c - Y):.4f}")
print(f"Dist center to Z: {np.linalg.norm(c - Z):.4f}")
print(f"Dist center to W: {np.linalg.norm(c - W):.4f} (diff with r: {np.linalg.norm(c - W) - r:.4e})")

# 7. Check pairwise distance between points
pts = {'A':A, 'B':B, 'C':C, 'D':D, 'O':O, 'P':P, 'Q':Q, 'R':R, 'E':E, 'X':X, 'Y':Y, 'Z':Z, 'W':W}
pt_list = list(pts.items())
min_d = 1e9
min_pair = None
for i in range(len(pt_list)):
    for j in range(i+1, len(pt_list)):
        d = np.linalg.norm(pt_list[i][1] - pt_list[j][1])
        if d < min_d:
            min_d = d
            min_pair = (pt_list[i][0], pt_list[j][0])

print(f"Min pairwise distance: {min_d:.2f} between {min_pair[0]} and {min_pair[1]}")
