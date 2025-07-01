import sys
input = sys.stdin.readline

N = int(input())
score = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(score[1])
    sys.exit()

elif N == 2:
    print(score[1] + score[2])
    sys.exit()

dp = [0] * (N + 1)
dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[1], score[2]) + score[3]

for i in range(4, N + 1):
    dp[i] = max(dp[i-2], dp[i-3] + score[i - 1]) + score[i]


print(dp[N])