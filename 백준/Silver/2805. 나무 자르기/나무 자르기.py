import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

lo, hi = 0, max(trees)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    
    if total >= M:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)