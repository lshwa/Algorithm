import sys
N = int(sys.stdin.readline())

ans = (N + 1) * N * (N - 1) // 2
print(ans)