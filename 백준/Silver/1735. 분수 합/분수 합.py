import sys
input = sys.stdin.readline
from math import gcd

A, B = map(int, input().split())
C, D = map(int, input().split())

numerator = (A * D) + (B * C)
denominator = B * D

g = gcd(numerator, denominator)

numerator //= g
denominator //= g

print(numerator, denominator)
