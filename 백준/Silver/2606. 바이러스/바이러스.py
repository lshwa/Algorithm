import sys
input = sys.stdin.readline

N = int(input())    # 컴퓨터 수
G = [[] for _ in range(N + 1)]  # 인접 리스트
E = int(input())    # 연결 쌍 수

for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    for nxt in G[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)
print(sum(visited) - 1)
