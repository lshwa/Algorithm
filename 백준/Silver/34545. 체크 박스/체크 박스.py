import sys
input = sys.stdin.readline

N = int(input())
present = list(map(int, input().split()))
target = list(map(int, input().split()))

ones = sum(target)
zeros = N - ones
all = (sum(present) == N)

# 1. 일일히 개수로 세는 방법
diff = 0
for a, b in zip(present, target):
    if a != b:
        diff += 1
sol1 = diff

# 2. 전체 체크 후에 목표처럼 되기 위해 한 개씩 빼는 방법
if all:
    sol2 = 0
else:
    sol2 = 1
sol2 += zeros

# 3. 전체 해제 후에 목표에서 1인 것만 체크
if all:
    sol3 = 1
else:
    sol3 = 2
sol3 += ones

print(min(sol1, sol2, sol3))
