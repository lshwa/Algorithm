def solution(array):
    max_value = max(array)
    max_index = array.index(max_value)
    answer = [max_value, max_index]
    
    return answer