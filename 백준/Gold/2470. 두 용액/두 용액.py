import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, n - 1
best_sum = 2_000_000_001
best_pair = (arr[l], arr[r])

while l < r:
    s = arr[l] + arr[r]

    if abs(s) < best_sum:
        best_sum = abs(s)
        best_pair = (arr[l], arr[r])
        if best_sum == 0:
            break

    if s < 0:
        l += 1
    else:
        r -= 1

print(best_pair[0], best_pair[1])