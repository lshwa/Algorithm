import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

if grid[0][0] == 0:
    print("No")
    sys.exit(0)

dirs = [(0, 1), (1, 0)]
visited = [[False] * N for _ in range(M)]
q = deque([(0, 0)])
visited[0][0] = True

ok = False
while q:
    r, c = q.popleft()
    if r == M - 1 and c == N - 1:
        ok = True
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == 1:
            visited[nr][nc] = True
            q.append((nr, nc))

print("Yes" if ok else "No")