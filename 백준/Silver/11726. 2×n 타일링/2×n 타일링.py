import sys
input = sys.stdin.readline

MOD = 10007
def count_tilings(n: int) -> int:
    if n == 1:
        return 1
    a, b = 1, 2        
    for _ in range(3, n+1):
        a, b = b, (a + b) % MOD
    return b % MOD

n = int(input())
print(count_tilings(n))