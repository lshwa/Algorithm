from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):
    M, N, K = map(int,input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[y][x] = True

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if field[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((nx, ny))
    
    count = 0
    for i in range(M):
        for j in range(N):
            if field[j][i] == 1 and not visited[j][i]:
                bfs(i, j)
                count += 1
    
    print(count)