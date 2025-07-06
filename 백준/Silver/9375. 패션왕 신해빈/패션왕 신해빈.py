import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    kind_cnt = {}
    for _ in range(N):
        _, kind = input().split()
        kind_cnt[kind] = kind_cnt.get(kind, 0) + 1
    
    answer = 1
    for c in kind_cnt.values():
        answer *= (c + 1)
    
    print(answer - 1)