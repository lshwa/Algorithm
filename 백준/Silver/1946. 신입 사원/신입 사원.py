import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort()

    cnt = 0
    best_interview = 10**9
    for doc, interview in arr:
        if interview < best_interview:
            cnt += 1
            best_interview = interview
    
    print(cnt)
