import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

def can_install(dist):
    count = 1
    last = houses[0]
    for i in range(1, N):
        if houses[i] - last >= dist:
            count += 1
            last = houses[i]

            if count >= C:
                return True
    return False

lo, hi = 1, houses[-1] - houses[0]
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_install(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
    
print(ans)