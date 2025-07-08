import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))

sorted_X = sorted(set(X))

rank = {num : idx for idx, num in enumerate(sorted_X)}

print(' '.join(str(rank[num]) for num in X))