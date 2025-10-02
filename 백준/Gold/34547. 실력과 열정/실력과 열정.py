import sys
input = sys.stdin.readline

N = int(input())
A0, B0, K = map(int, input().split())
total = A0 + B0

def score(a):
    return a * (total - a)

# 다이내믹 프로그래밍 문제인듯..? 
# A를 기준으로 늘려나가거나, 좁혀나가면서 max 값으로 찾기
NEG = -10 ** 18
prev = [NEG] * (total + 1)
prev[A0] = 0

for day in range(1, N + 1):
    pref = [NEG] * (total + 1)
    suff = [NEG] * (total + 1)

    best = NEG
    for a in range(total + 1):
        if prev[a] > best:
            best = prev[a]
        pref[a] = best
    
    best = NEG
    for a in range(total, -1, -1):
        if prev[a] > best:
            best = prev[a]
        suff[a] = best
    
    curr = [NEG] * (total + 1)
    for a in range(total + 1):
        cand = NEG
        left = a - K
        if left >= 0:
            cand = max(cand, pref[left])
        right = a + K
        if right <= total:
            cand = max(cand, suff[right])
        
        if cand!= NEG:
            curr[a] = cand + score(a)
    prev = curr

print(max(prev))

