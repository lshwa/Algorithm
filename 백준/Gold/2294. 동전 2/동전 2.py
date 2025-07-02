import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

INF = 10 ** 10
dp = [INF] * (K + 1)
dp[0] = 0

for c in coins:
    for x in range(c, K + 1):
        if dp[x - c] + 1 < dp[x]:
            dp[x] = dp[x - c] + 1

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])
