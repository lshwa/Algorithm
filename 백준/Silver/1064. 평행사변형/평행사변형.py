import math

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def is_colinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])

xA, yA, xB, yB, xC, yC = map(int, input().split())
A, B, C = (xA, yA), (xB, yB), (xC, yC)

if is_colinear(A, B, C):
    print(-1)

else:
    perimeters = []

    # 경우 1: A, B 기준 → D = C + (B - A)
    dx1 = B[0] - A[0]
    dy1 = B[1] - A[1]
    D1 = (C[0] + dx1, C[1] + dy1)
    p1 = dist(A, B) + dist(B, D1) + dist(D1, C) + dist(C, A)
    perimeters.append(p1)

    # 경우 2: B, C 기준 → D = A + (C - B)
    dx2 = C[0] - B[0]
    dy2 = C[1] - B[1]
    D2 = (A[0] + dx2, A[1] + dy2)
    p2 = dist(B, C) + dist(C, D2) + dist(D2, A) + dist(A, B)
    perimeters.append(p2)

    # 경우 3: C, A 기준 → D = B + (A - C)
    dx3 = A[0] - C[0]
    dy3 = A[1] - C[1]
    D3 = (B[0] + dx3, B[1] + dy3)
    p3 = dist(C, A) + dist(A, D3) + dist(D3, B) + dist(B, C)
    perimeters.append(p3)

    print(max(perimeters) - min(perimeters))