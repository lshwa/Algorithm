import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def dfs(x, y, size):
    global white, blue
    first = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                half = size // 2
                dfs(x, y, half)
                dfs(x, y + half, half)
                dfs(x + half, y, half)
                dfs(x + half, y + half, half)
                return

    if first == 0:
        white += 1
    else:
        blue += 1

dfs(0, 0, N)
print(white)
print(blue)