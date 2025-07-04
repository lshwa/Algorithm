import sys
input = sys.stdin.readline

N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]
answer = 0

for i in reversed(money):
    if i <= K:
        answer += K // i
        K %= i
        if K == 0:
            break

print(answer)