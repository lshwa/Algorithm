import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
list = deque(range(1, N + 1))

while len(list) > 1:
    list.popleft()
    list.append(list.popleft())

print(list[0])