import sys

input == sys.stdin.readline

n, m = map(int, input().split())
set_n = set()

for _ in range(n):
    line = input().strip()
    set_n.add(line)

answer = 0
for _ in range(m):
    line = input().strip()
    if line in set_n:
        answer += 1
    

print(answer)