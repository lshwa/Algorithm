def solution(num_str):
    answer = 0
    
    for list in num_str:
        answer += int(list)
    
    return answer