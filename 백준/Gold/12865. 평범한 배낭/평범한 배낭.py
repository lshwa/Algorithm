N, K = map(int, input().split())
w = [0] * (N + 1)
v = [0] * (N + 1)

for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for c in range(1, K + 1):
        if w[i] <= c:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c - w[i]] + v[i])
        else:
            dp[i][c] = dp[i-1][c]

print(dp[N][K])
