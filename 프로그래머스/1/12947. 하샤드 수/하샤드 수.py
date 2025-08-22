def solution(x):
    answer = True
    
    str_x = str(x)
    sum_x = 0
    for i in range(0, len(str_x)):
        sum_x += int(str_x[i])
    
    if x % sum_x != 0:
        return False
    
    return answer