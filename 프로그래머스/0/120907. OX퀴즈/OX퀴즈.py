def solution(quiz):
    answer = []
    
    for q in quiz:
        a, op, b, eq, result = q.split()
        a, b, result = int(a), int(b), int(result)
        
        if op == '+':
            val = a + b
        else:
            val = a - b
        
        answer.append("O" if val == result else "X")
    
    return answer
