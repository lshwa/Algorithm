def solution(box, n):
    answer = 0
    
    a, b, c = (box[i] // n for i in range(0, 3))
    answer = a * b * c
    
    return answer