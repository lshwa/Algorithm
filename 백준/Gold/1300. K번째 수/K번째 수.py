import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

lo, hi = 1, k
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    count = 0

    for i in range(1, N + 1):
        count += min(N, mid // i)

    if count >= k:
        ans = mid
        hi = mid - 1
    
    else:
        lo = mid + 1
print(ans)