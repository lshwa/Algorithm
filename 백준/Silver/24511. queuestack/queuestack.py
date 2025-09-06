from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))   
M = int(input())
C = list(map(int, input().split()))

dq = deque()

for a, b in zip(A, B):
    if a == 0:
        dq.appendleft(b)

dq.extend(C)

result = [dq.popleft() for _ in range(M)]
print(*result)