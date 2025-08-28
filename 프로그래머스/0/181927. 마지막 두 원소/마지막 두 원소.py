def solution(num_list):
    answer = []
    size = len(num_list)
    
    if num_list[size - 2] >= num_list[size - 1]:
        num_list.append(num_list[size - 1] * 2)
    elif num_list[size - 2] < num_list[size - 1]:
        num_list.append(num_list[size - 1] - num_list[size - 2])
    
    answer = num_list
    return answer