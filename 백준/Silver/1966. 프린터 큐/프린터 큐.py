from collections import deque

test = int(input())

for _ in range(test):
    n, target = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque()
    for i in range(n):
        queue.append((i, priorities[i]))

    count = 0

    while queue:
        cur = queue.popleft()
        
        has_higher = False
        for q in queue:
            if q[1] > cur[1]:  
                has_higher = True
                break
        
        if has_higher:
            queue.append(cur) 
        else:
            count += 1  
            if cur[0] == target:
                print(count)
                break