import sys
input = sys.stdin.readline

n = int(input().strip())

print("YES")

black, white = [], []
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            black.append((i, j))
        else:
            white.append((i, j))

order = []
# 1은 검은색에서 시작
if black:
    order.append(black.pop())

# 이후는 흰색 2칸, 검은색 2칸을 번갈아 채운다
take_white = True
while black or white:
    bag = white if take_white else black
    for _ in range(2):
        if bag:
            order.append(bag.pop())
    take_white = not take_white

# order에 따라 번호 배치
grid = [[0]*n for _ in range(n)]
for num, (r, c) in enumerate(order, start=1):
    grid[r][c] = num

# 출력
for r in range(n):
    print(*grid[r])
