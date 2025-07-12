import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
follow = [0] * (N + 1)
for i in range(1, N + 1):
    follow[i] = int(input())

def dfs(start, visited):
    count = 0
    cur = start
    while not visited[cur]:
        visited[cur] = True
        cur = follow[cur]
        count += 1
    return count

max_count = 0
answer = 0

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    count = dfs(i, visited)
    if count > max_count:
        max_count = count
        answer = i

print(answer)