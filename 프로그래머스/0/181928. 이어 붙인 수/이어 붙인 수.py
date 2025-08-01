def solution(num_list):
    answer = 0
    
    odd_num = ''
    even_num = ''
    
    for i in range(0, len(num_list)):
        if num_list[i] % 2 == 0:
            even_num += str(num_list[i])
        else:
            odd_num += str(num_list[i])
            
    answer = int(odd_num) + int(even_num)
    
    return answer