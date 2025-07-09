import sys
from math import gcd
from functools import reduce
input = sys.stdin.readline

N = int(input())
col = sorted(int(input()) for _ in range(N))

diffs = [col[i] - col[i - 1] for i in range(1, N)]
g = reduce(gcd, diffs)

add = sum(d // g - 1 for d in diffs)
print(add)
