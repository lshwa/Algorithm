import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000000

dp = [[0] * 10 for _ in range(N + 1)]

for d in range(1, 10):
    dp[1][d] = 1

for n in range(2, N+1):
    for d in range(10):
        if d == 0:
            dp[n][d] = dp[n-1][1]
        elif d == 9:
            dp[n][d] = dp[n-1][8]
        else:
            dp[n][d] = (dp[n-1][d-1] + dp[n-1][d+1]) % MOD

print(sum(dp[N]) % MOD)