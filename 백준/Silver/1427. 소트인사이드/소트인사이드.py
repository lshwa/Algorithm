import sys
input = sys.stdin.readline

num = input().strip()
digits = sorted(num, reverse = True)

print(''.join(digits))