import sys
input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
M = int(input())

# 1. 최대 요청이 상한
if sum(req) < M:
    print(max(req))
    sys.exit(0)

# 2. 초과 되는 경우
lo, hi = 0, max(req)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    total = 0
    for x in req:
        total += x if x < mid else mid
        if total > M:
            break
    
    if total <= M:
        ans = mid
        lo = mid + 1
    
    else:
        hi = mid - 1
    
print(ans)