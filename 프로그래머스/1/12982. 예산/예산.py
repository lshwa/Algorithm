def solution(d, budget):
    d.sort()
    
    total = 0
    count = 0
    
    for cost in d:
        if total + cost > budget:
            break
        total += cost
        count += 1
    return count