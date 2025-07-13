from collections import deque

A, K = map(int, input().split())
visited = set()
queue = deque()
queue.append((A, 0))

while queue:
    current, cnt = queue.popleft()
    if current == K:
        print(cnt)
        break
    
    if current + 1 <= K and (current + 1) not in visited:
        visited.add(current + 1)
        queue.append((current + 1, cnt + 1))
    
    if current * 2 <= K and (current * 2) not in visited:
        visited.add(current * 2)
        queue.append((current * 2 , cnt + 1))
