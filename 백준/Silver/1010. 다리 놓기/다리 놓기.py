import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    result = (math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))
    print(int(result))
