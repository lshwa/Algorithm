import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0] * (M + 1)

for _ in range(N):
    row = list(map(int, input().split()))
    prev_diag = 0
    for c in range(1, M + 1):
        up = dp[c]
        left = dp[c - 1]
        diag = prev_diag
        temp = up

        dp[c] = max(up, left, diag) + row[c - 1]
        prev_diag = temp 

print(dp[M])