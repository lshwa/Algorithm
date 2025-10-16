def solution(x, n):
    answer = []
    curr = 0
    
    for i in range(n):
        curr += x
        answer.append(curr)
    
    return answer