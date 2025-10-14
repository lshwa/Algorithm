def solution(q, r, code):
    answer = ''
    
    for index, ch in enumerate(code):
        if index % q == r:
            answer += ch
    
    return answer