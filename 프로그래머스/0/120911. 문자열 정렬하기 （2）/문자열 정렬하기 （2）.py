def solution(my_string):
    my_string = my_string.lower()
    sorted_chars = sorted(my_string)
    answer = ''.join(sorted_chars)
    
    return answer
