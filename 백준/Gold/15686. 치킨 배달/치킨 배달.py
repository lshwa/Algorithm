import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
houses, shops = [], []

for r in range(N):
    row = list(map(int, input().split()))
    for c, v in enumerate(row):
        if v == 1:
            houses.append((r, c))
        elif v == 2:
            shops.append((r, c))

def city_distance(selected):
    total = 0
    for hr, hc in houses:
        best = min(abs(hr - sr) + abs(hc - sc) for sr, sc in selected)
        total += best

    return total

ans = float('inf')
for comb in combinations(shops, M):
    ans = min(ans, city_distance(comb))

print(ans)
