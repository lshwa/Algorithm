from collections import Counter

def solution(k, tangerine):
    answer = 0
    total = 0
    
    counter = Counter(tangerine)
    counts = sorted(counter.values(), reverse = True)
    
    for item in counts:
        if total >= k:
            break
        total += item
        answer += 1
    
    return answer
        
        