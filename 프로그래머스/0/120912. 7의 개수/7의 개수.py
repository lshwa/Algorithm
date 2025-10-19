def solution(array):
    answer = 0
    
    for item in array:
        item = str(item)
        for ch in item:
            if ch == '7':
                answer += 1
    
    return answer