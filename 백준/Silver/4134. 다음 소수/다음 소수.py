import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)