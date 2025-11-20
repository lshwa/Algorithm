def solution(l, r):
    answer = []
    
    for x in range(l, r + 1):
        s = str(x)
        if all(ch in ('0', '5') for ch in s):
            answer.append(x)
    
    if not answer:
        return [-1]
    return answer