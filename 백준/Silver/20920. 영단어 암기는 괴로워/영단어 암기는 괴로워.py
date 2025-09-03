import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

filtered = [w for w in words if len(w) >= M]
cnt = Counter(filtered)

sorted_words = sorted(cnt.keys(), key = lambda w : (-cnt[w], -len(w), w))
print("\n".join(sorted_words))