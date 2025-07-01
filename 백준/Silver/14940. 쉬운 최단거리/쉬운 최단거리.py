import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
start = None 

for r in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    if 2 in row:
        start = (r, row.index(2))

dist = [[-1]*M for _ in range(N)]
dq = deque()

sr, sc = start
dist[sr][sc] = 0
dq.append((sr,sc))

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

while dq:
    r, c = dq.popleft()
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 0:
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dq.append((nr, nc))

for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            dist[r][c] = 0
    print(*dist[r])