import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

window_sum = sum(temp[:K])
answer = window_sum

for i in range(K, N):
    window_sum += temp[i] - temp[i - K]
    answer = max(answer, window_sum)

print(answer)