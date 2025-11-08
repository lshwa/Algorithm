import math

def solution(n, m):
    gcd_val = math.gcd(n, m)
    lcm_val = abs(n * m) // gcd_val
    return [gcd_val, lcm_val]

