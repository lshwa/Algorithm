def solution(my_string):
    
    answer = [int(ch) for ch in my_string if ch.isdigit()]
    answer.sort()
    
    return answer