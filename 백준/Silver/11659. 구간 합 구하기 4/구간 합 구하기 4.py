import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + lst[i - 1]

for _ in range(M):
    a, b = map(int,input().split())
    print(prefix[b] - prefix[a - 1])