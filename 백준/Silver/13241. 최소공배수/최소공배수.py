import sys
input = sys.stdin.readline
from math import gcd

A, B = map(int, input().split())
answer = A * B // gcd(A, B)

print(answer)