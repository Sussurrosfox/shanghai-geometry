import numpy as np
import matplotlib.pyplot as plt

# The candidate points:
P = np.array([240.00, 90.00])
Q = np.array([80.00, 360.00])
A = np.array([315.32, 296.95])
B = np.array([377.71, 468.36])
C = np.array([636.52, 562.56])
D = np.array([395.60, 275.44])
O = np.array([388.03, 357.07])
R = np.array([161.34, 222.74])
E = np.array([182.47, 187.08])
X = np.array([273.46, 181.93])
Y = np.array([107.71, 370.09])
Z = np.array([272.86, 129.16])
W = np.array([190.21, 330.47])
center = np.array([56.63, 158.00])
radius = 218.15

# Let's inspect the geometric relations:
print("Geometric Verifications:")
# 1. P, A, B collinear?
vAB = B - A
vAP = P - A
cross_PAB = vAB[0]*vAP[1] - vAB[1]*vAP[0]
print(f"Collinear P, A, B cross: {cross_PAB:.4e}")

# 2. P, D, C collinear?
vCD = D - C
vCP = P - C
cross_PDC = vCD[0]*vCP[1] - vCD[1]*vCP[0]
print(f"Collinear P, D, C cross: {cross_PDC:.4e}")

# 3. Q, A, D collinear?
vAD = D - A
vAQ = Q - A
cross_QAD = vAD[0]*vAQ[1] - vAD[1]*vAQ[0]
print(f"Collinear Q, A, D cross: {cross_QAD:.4e}")

# 4. Q, B, C collinear?
vBC = C - B
vBQ = Q - B
cross_QBC = vBC[0]*vBQ[1] - vBC[1]*vBQ[0]
print(f"Collinear Q, B, C cross: {cross_QBC:.4e}")

# 5. O is AC intersect BD?
vAC = C - A
vAO = O - A
cross_ACO = vAC[0]*vAO[1] - vAC[1]*vAO[0]
vBD = D - B
vBO = O - B
cross_BDO = vBD[0]*vBO[1] - vBD[1]*vBO[0]
print(f"O on AC cross: {cross_ACO:.4e}, O on BD cross: {cross_BDO:.4e}")

# 6. OR perp PQ?
vPQ = Q - P
vOR = R - O
dot_OR_PQ = np.dot(vOR, vPQ)
print(f"OR perp PQ dot: {dot_OR_PQ:.4e}")

# 7. R on PQ?
vPR = R - P
cross_PQR = vPQ[0]*vPR[1] - vPQ[1]*vPR[0]
print(f"R on PQ cross: {cross_PQR:.4e}")

# 8. E on AC and PQ?
vAE = E - A
cross_ACE = vAC[0]*vAE[1] - vAC[1]*vAE[0]
vPE = E - P
cross_PQE = vPQ[0]*vPE[1] - vPQ[1]*vPE[0]
print(f"E on AC cross: {cross_ACE:.4e}, E on PQ cross: {cross_PQE:.4e}")

# 9. Harmonic ratio (C, A; O, E) = -1 ?
# Since C, O, A, E are collinear, let's measure signed distances from A along vector (C-A):
uAC = vAC / np.linalg.norm(vAC)
dC = np.dot(C - A, uAC)
dO = np.dot(O - A, uAC)
dA = 0.0
dE = np.dot(E - A, uAC)
# Cross ratio (C, A; O, E) = ( (dO-dC)/(dO-dA) ) / ( (dE-dC)/(dE-dA) )
cross_ratio = ((dO - dC) / (dO - dA)) / ((dE - dC) / (dE - dA))
print(f"Harmonic cross ratio (C, A; O, E): {cross_ratio:.6f} (target: -1.000000)")
print(f"Ratio AO/OC = {abs(dO-dA)/abs(dC-dO):.4f}, AE/EC = {abs(dE-dA)/abs(dC-dE):.4f}")

# 10. Distances from circle center to X, Y, Z, W:
print("Distances to circle center:")
for name, pt in [('X', X), ('Y', Y), ('Z', Z), ('W', W)]:
    d = np.linalg.norm(pt - center)
    print(f"  |center - {name}| = {d:.4f} (diff with r: {d - radius:.4e})")

# Let's inspect angles:
# Angle ARO vs Angle CRO:
vRA = A - R; vRO = O - R; vRC = C - R
cos_ARO = np.dot(vRA, vRO) / (np.linalg.norm(vRA) * np.linalg.norm(vRO))
cos_CRO = np.dot(vRC, vRO) / (np.linalg.norm(vRC) * np.linalg.norm(vRO))
ang_ARO = np.degrees(np.arccos(np.clip(cos_ARO, -1, 1)))
ang_CRO = np.degrees(np.arccos(np.clip(cos_CRO, -1, 1)))
print(f"Angle ARO: {ang_ARO:.4f} deg, Angle CRO: {ang_CRO:.4f} deg (diff: {ang_ARO - ang_CRO:.4e})")

# Angle ARQ vs Angle CRP:
vRQ = Q - R; vRP = P - R
cos_ARQ = np.dot(vRA, vRQ) / (np.linalg.norm(vRA) * np.linalg.norm(vRQ))
cos_CRP = np.dot(vRC, vRP) / (np.linalg.norm(vRC) * np.linalg.norm(vRP))
ang_ARQ = np.degrees(np.arccos(np.clip(cos_ARQ, -1, 1)))
ang_CRP = np.degrees(np.arccos(np.clip(cos_CRP, -1, 1)))
print(f"Angle ARQ: {ang_ARQ:.4f} deg, Angle CRP: {ang_CRP:.4f} deg (diff: {ang_ARQ - ang_CRP:.4e})")
