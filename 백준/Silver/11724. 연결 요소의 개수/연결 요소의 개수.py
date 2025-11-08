import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N + 1):
    if adj[i]:
        adj[i].sort()

visited = [False] * (N + 1)

def dfs_iter(start):
    stack = [start]
    visited[start] = True
    while stack:
        v = stack.pop()
        for nv in adj[v]:
            if not visited[nv]:
                visited[nv] = True
                stack.append(nv)

components = 0
for v in range(1, N + 1):
    if not visited[v]:
        components += 1
        dfs_iter(v)

print(components)