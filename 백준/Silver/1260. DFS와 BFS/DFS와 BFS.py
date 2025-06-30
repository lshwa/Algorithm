from collections import defaultdict, deque
import sys

input = sys.stdin.readline

graph = defaultdict(list)
N, M, V = map(int, input().split())

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)          

for v in range(1, N + 1):
    graph[v].sort()

# DFS 
def dfs(start):
    visited, stack = set(), [start]
    order = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            order.append(v)
            stack.extend(reversed(graph[v]))
    return order

# BFS
def bfs(start):
    visited, q = {start}, deque([start])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in graph[v]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return order

print(" ".join(map(str, dfs(V))))
print(" ".join(map(str, bfs(V))))