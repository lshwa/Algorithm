import sys
input = sys.stdin.readline


def is_promising(num):
    if num < 2:              
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())
answer = []

for i in range(M, N + 1):
    if is_promising(i):
        answer.append(i)
    else:
        continue

print("\n".join(map(str,answer)))
