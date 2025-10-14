def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str), n):
        split = my_str[i:i + n]
        answer.append(split)
    
    return answer