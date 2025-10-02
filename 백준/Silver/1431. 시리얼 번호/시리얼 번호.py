import sys
input = sys.stdin.readline

N = int(input())
guitar = [input().strip() for _ in range(N)]

def digit_sum(s):
    return sum(int(ch) for ch in s if ch.isdigit())
            
guitar.sort(key = lambda s : (len(s), digit_sum(s), s))

for g in guitar:
    print(g)