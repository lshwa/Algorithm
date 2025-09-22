def solution(n):
    MOD = 1234567
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
        
    return b % MOD if n >= 1 else a % MOD
