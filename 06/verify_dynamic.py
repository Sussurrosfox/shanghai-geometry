import numpy as np

# Let's verify the exact dynamic coordinate generation
# We can define the 4 lines by P, Q, and 4 angles, or by A, B, C, D directly
# If we define:
# P = { x: 450.0, y: 70.0 }
# Q = { x: 60.0, y: 400.0 }
# A = { x: 295.98, y: 289.96 }
# B = { x: 255.64, y: 347.58 }
# D = { x: 506.74, y: 191.68 }
# Then line PAB is P + t*(B-P)
# line PDC is P + s*(D-P)
# line QAD is Q + u*(A-Q)
# line QBC is Q + v*(B-Q)
# Then C is intersection of PDC and QBC!
# Let's verify this in Python:

def line_inter(p1, d1, p2, d2):
    det = d1[0]*(-d2[1]) - d1[1]*(-d2[0])
    t = ((p2[0]-p1[0])*(-d2[1]) - (p2[1]-p1[1])*(-d2[0])) / det
    return p1 + t * d1

def foot(p, a, b):
    ab = b - a
    return a + np.dot(p - a, ab) / np.dot(ab, ab) * ab

def circle3(p1, p2, p3):
    d = 2 * (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))
    ux = ((p1[0]**2 + p1[1]**2)*(p2[1]-p3[1]) + (p2[0]**2 + p2[1]**2)*(p3[1]-p1[1]) + (p3[0]**2 + p3[1]**2)*(p1[1]-p2[1])) / d
    uy = ((p1[0]**2 + p1[1]**2)*(p3[0]-p2[0]) + (p2[0]**2 + p2[1]**2)*(p1[0]-p3[0]) + (p3[0]**2 + p3[1]**2)*(p2[0]-p1[0])) / d
    c = np.array([ux, uy])
    return c, np.linalg.norm(c - p1)

P = np.array([450.0, 70.0])
Q = np.array([60.0, 400.0])
A = np.array([295.98, 289.96])
B = np.array([255.64, 347.58])
D = np.array([506.74, 191.68])

# C is intersection of PD (line P-D) and QB (line Q-B)
C = line_inter(P, D - P, Q, B - Q)
O = line_inter(A, C - A, B, D - B)
R = foot(O, P, Q)
E = line_inter(A, C - A, P, Q - P)

X = foot(R, A, B)
Y = foot(R, B, C)
Z = foot(R, C, D)
W = foot(R, D, A)

center, rad = circle3(X, Y, Z)
print("Dynamic Evaluation:")
print("C:", C)
print("O:", O)
print("R:", R)
print("E:", E)
print("X:", X)
print("Y:", Y)
print("Z:", Z)
print("W:", W)
print("Circle center:", center, "radius:", rad)
print("Diff W to circle:", abs(np.linalg.norm(center - W) - rad))

# Check angles:
def angle(v1, v2):
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(np.clip(cos, -1, 1)))

print("ang ARO:", angle(A - R, O - R))
print("ang CRO:", angle(C - R, O - R))
print("ang ARQ:", angle(A - R, Q - R))
print("ang CRP:", angle(C - R, P - R))
