import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

dp = [0] * 21
dp[arr[0]] = 1

for i in range(1, N - 1):
    x = arr[i]
    next = [0] * 21
    for s in range(21):
        if dp[s] == 0:
            continue
        if 0 <= s + x <= 20:
            next[s + x] += dp[s]
        if 0 <= s - x <= 20:
            next[s - x] += dp[s]
    dp = next

target = arr[-1]
print(dp[target])