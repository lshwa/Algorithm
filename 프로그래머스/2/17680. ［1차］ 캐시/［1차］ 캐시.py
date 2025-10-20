from collections import deque

def solution(cacheSize,cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = deque()
    totaltime = 0
    
    for city in cities:
        c = city.lower()
    
        if c in cache:
            totaltime += 1
            cache.remove(c)
            cache.append(c)
        else:
            totaltime += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(c)

    return totaltime