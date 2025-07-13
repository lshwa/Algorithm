import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
floor = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(x, y, symbol):
    visited[x][y] = True
    if symbol == '-':
        if y + 1 < m and not visited[x][y + 1] and floor[x][y + 1] == '-':
            dfs(x, y+1, symbol)
    elif symbol == '|':
        if x + 1 < n and not visited[x+1][y] and floor[x + 1][y] == '|':
            dfs(x + 1, y, symbol)

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, floor[i][j])
            count += 1

print(count)