import sys
input = sys.stdin.readline

N, K = map(int, input().split())
friends = [int(input()) for _ in range(N)]

visited = [False] * N
now = 0
count = 0

while not visited[now]:
    if now == K:
        print(count)
        break       # 목표 대상 만남
    visited[now] = True
    now = friends[now]
    count += 1
else:
    print(-1)