import sys
input = sys.stdin.readline

N, K = map(int, input().split())
mod = 10007

dp = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(N + 1):
    for k in range(min(n, K) + 1):
        if k == 0 or k == n:
            dp[n][k] = 1
        else:
            dp[n][k] = (dp[n-1][k-1] + dp[n-1][k]) % mod

print(dp[N][K])
