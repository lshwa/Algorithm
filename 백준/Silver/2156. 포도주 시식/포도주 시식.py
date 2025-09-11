import sys
input = sys.stdin.readline

n = int(input().strip())
w = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(w[1])

elif n == 2:
    print(w[1] + w[2])

else:
    dp = [0] * (n + 1)
    dp[1] = w[1]
    dp[2] = w[1] + w[2]
    dp[3] = max(dp[2], w[1] + w[3], w[2] + w[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i])

    print(dp[n])