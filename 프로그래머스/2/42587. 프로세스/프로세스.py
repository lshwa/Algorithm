from collections import deque

def solution(priorities, location):
    processes = []
    for index, priority in enumerate(priorities):
        processes.append((priority, index))
        
    q = deque(processes)
    answer = 0
    
    while q:
        current_priority, current_index = q.popleft()
        
        if any(current_priority < other_priority for other_priority, _ in q):
            q.append((current_priority, current_index))
        else:
            answer += 1
            if current_index == location:
                return answer