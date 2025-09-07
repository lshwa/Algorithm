import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lis = []
pos = [0] * N

for i in range(N):
    x = A[i]
    if not lis or lis[-1] < x:
        lis.append(x)
        pos[i] = len(lis) - 1
    else:
        idx = bisect.bisect_left(lis, x)
        lis[idx] = x
        pos[i] = idx

L = len(lis)
print(L)

ans = []
target = L - 1
for i in range(N - 1, -1, -1):
    if pos[i] == target:
        ans.append(A[i])
        target -= 1
        if target < 0:
            break

print(" ".join(map(str,ans[::-1])))
    