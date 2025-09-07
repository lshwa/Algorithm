import sys
input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()

two_sum = set()
for i in range(N):
    for j in range(i, N):
        two_sum.add(U[i] + U[j])

for k in reversed(U):
    for x in U:
        if k - x in two_sum:
            print(k)
            sys.exit(0)