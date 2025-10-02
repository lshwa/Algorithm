import sys
input = sys.stdin.readline

M = int(input())

left = list(range(1, M + 1))
right = list(range(M, 0, -1))
answer = left + right

print(*answer)