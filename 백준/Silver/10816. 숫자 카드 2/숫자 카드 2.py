import sys
from collections import Counter
read = sys.stdin.readline

N = int(read())
cards = list(map(int, read().split()))
cnt = Counter(cards)

M = int(read())
score_cards = list(map(int, read().split()))

out = [str(cnt.get(x, 0)) for x in score_cards]
print(" ".join(out))
