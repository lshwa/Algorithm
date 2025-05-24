def solution(num_list):
    answer = []
    even_number = 0
    odd_number = 0
    
    for i in num_list:
        if (i % 2 == 0):
            even_number += 1
        else:
            odd_number += 1
            
    answer.append(even_number)
    answer.append(odd_number)
    return answer