import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [0] * (max_n + 3)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
out = [str(dp[n]) for n in nums]
print("\n".join(out))