def solution(num_list):
    answer = 0
    
    for list in num_list:
        if list < 0:
            return num_list.index(list)
        
    return -1