import heapq

def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        if not works:
            break
        max_work = heapq.heappop(works)
        if max_work == 0:
            break
        heapq.heappush(works, max_work + 1)  
    
    return sum(w ** 2 for w in works)