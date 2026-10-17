import numpy as np

P = np.array([508.36, 78.68])
Q = np.array([127.14, 485.75])
A = np.array([387.02, 331.81])
B = np.array([356.41, 395.68])
C = np.array([624.72, 290.26])
D = np.array([583.55, 215.40])
O = np.array([450.95, 320.64])
R = np.array([360.82, 236.23])
E = np.array([248.65, 356.00])
X = np.array([419.38, 264.30])
Y = np.array([414.50, 372.85])
Z = np.array([540.62, 137.34])
W = np.array([409.54, 318.47])
center = np.array([612.53, 327.38])
radius = 203.18

# Check lines:
# Line P-A-B?
# Vector PA vs PB:
vPA = A - P; vPB = B - P
print("Line PAB cross:", vPA[0]*vPB[1] - vPA[1]*vPB[0])

# Line P-D-C?
vPD = D - P; vPC = C - P
print("Line PDC cross:", vPD[0]*vPC[1] - vPD[1]*vPC[0])

# Line Q-A-D?
# In earlier code: A = L_P1 inter L_Q1, D = L_P2 inter L_Q1 -> Q, A, D collinear!
vQA = A - Q; vQD = D - Q
print("Line QAD cross:", vQA[0]*vQD[1] - vQA[1]*vQD[0])

# Line Q-B-C?
vQB = B - Q; vQC = C - Q
print("Line QBC cross:", vQB[0]*vQC[1] - vQB[1]*vQC[0])

# O = AC inter BD?
vAC = C - A; vAO = O - A
print("O on AC cross:", vAC[0]*vAO[1] - vAC[1]*vAO[0])
vBD = D - B; vBO = O - B
print("O on BD cross:", vBD[0]*vBO[1] - vBD[1]*vBO[0])

# R = foot(O, PQ)?
vPQ = Q - P; vOR = R - O
print("OR dot PQ:", np.dot(vOR, vPQ))
vPR = R - P
print("R on PQ cross:", vPQ[0]*vPR[1] - vPQ[1]*vPR[0])

# E = AC inter PQ?
vPE = E - P
print("E on PQ cross:", vPQ[0]*vPE[1] - vPQ[1]*vPE[0])
vAE = E - A
print("E on AC cross:", vAC[0]*vAE[1] - vAC[1]*vAE[0])

# X, Y, Z, W feet:
# X on AB?
print("RX dot AB:", np.dot(X - R, B - A))
# Y on BC?
print("RY dot BC:", np.dot(Y - R, C - B))
# Z on CD?
print("RZ dot CD:", np.dot(Z - R, C - D))
# W on DA?
print("RW dot DA:", np.dot(W - R, A - D))

# Distance of X, Y, Z, W to center:
for n, pt in [('X', X), ('Y', Y), ('Z', Z), ('W', W)]:
    d = np.linalg.norm(pt - center)
    print(f"|center - {n}| = {d:.4f}, diff = {d - radius:.4e}")

# Angles:
def angle(v1, v2):
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(np.clip(cos, -1, 1)))

print("ang ARO:", angle(A - R, O - R))
print("ang CRO:", angle(C - R, O - R))
print("ang ARQ:", angle(A - R, Q - R))
print("ang CRP:", angle(C - R, P - R))
