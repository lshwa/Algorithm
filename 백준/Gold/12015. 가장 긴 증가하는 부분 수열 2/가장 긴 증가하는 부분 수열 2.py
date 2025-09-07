import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = []
for x in arr:
    if not lis or lis[-1] < x:
        lis.append(x)
    else:
        idx = bisect.bisect_left(lis, x)
        lis[idx] = x

print(len(lis))