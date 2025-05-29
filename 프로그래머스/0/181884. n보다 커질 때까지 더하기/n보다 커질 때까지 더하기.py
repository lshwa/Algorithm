def solution(numbers, n):
    answer = 0
    total = 0
    
    for i in numbers:
        if (total > n):
            break
        total += i
    
    answer = total
    
    return answer