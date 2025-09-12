import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ps = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, m + 1):
        row_sum += arr[i - 1][j - 1]
        ps[i][j] = ps[i - 1][j] + row_sum

k = int(input().strip())
for _ in range(k):
    i , j, x, y = map(int, input().split())
    s = ps[x][y] - ps[i - 1][y] - ps[x][j - 1] + ps[i - 1][j - 1]
    print(s)

