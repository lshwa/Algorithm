import sys
input = sys.stdin.readline

T = int(input())
tri = [int(input()) for _ in range(T)]
max_tri = max(tri)
answer = []

dp = [0] * max(4, max_tri + 1)  
dp[1] = dp[2] = dp[3] = 1

for i in range(4, max_tri + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in tri:
    print(dp[n])


