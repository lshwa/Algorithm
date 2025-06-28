import math

T = int(input())
answer = 0 

for _ in range(T):
    A, B = map(int, input().split())
    answer = A * B // math.gcd(A, B)
    print(answer)
    