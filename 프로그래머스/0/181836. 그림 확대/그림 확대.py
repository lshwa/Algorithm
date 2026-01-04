def solution(picture, k):
    answer = []
    
    for line in picture:
        expanded = ''
        for c in line:
            expanded += c * k
        
        for _ in range(k):
            answer.append(expanded)
    
    return answer