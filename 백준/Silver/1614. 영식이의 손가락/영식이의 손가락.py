import sys
input = sys.stdin.readline

finger = int(input().strip())
n = int(input().strip())
answer = 0

if finger == 1:
    if n == 0:
        answer = 0
    else:
        answer = 8 * n

elif finger == 5:
    if n == 0:
        answer = 4
    else:
        answer = 8 * n + 4

elif finger == 3:
    if n == 0:
        answer = 2
    else:
        answer = 4 * n + 2

elif finger == 2:
    if n == 0:
        answer = 1
    elif n % 2 == 1:
        k = (n + 1) // 2
        answer = 8 * k - 1
    else:
        k = n // 2
        answer = 8 * k + 1

elif finger == 4:
    if n == 0:
        answer = 3
    elif n % 2 == 1:
        k = (n + 1) // 2
        answer = 8 * k - 3
    else:
        k = n // 2
        answer = 8 * k + 3

print(answer)
