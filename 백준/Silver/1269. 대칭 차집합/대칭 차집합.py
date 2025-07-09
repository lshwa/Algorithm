import sys
input = sys.stdin.readline

a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
answer = len(set_a) + len(set_b)

for i in set_a:
    if i in set_b:
        answer -= 2

print(answer)