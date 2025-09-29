import sys
input = sys.stdin.readline

N = int(input())

dp = [False] * (max(N, 4) + 1)
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, N + 1):
    dp[i] = (not dp[i - 1]) or (not dp[i - 3]) or (not dp[i - 4])
    
if dp[N] == True:
    print("SK")
else:
    print("CY")