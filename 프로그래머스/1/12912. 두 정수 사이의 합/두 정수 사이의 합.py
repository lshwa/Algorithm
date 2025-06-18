def solution(a, b):
    answer = 0
    max_number = max(a, b)
    min_number = min(a, b)
    
    for i in range(min_number, max_number + 1):
        answer += i
    
    
    return answer