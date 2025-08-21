def solution(n):
    list = []
    for x in range(1, n):
        if n % x == 1:
            list.append(x)
    
    list.sort()
    answer = list[0]
    
    
    return answer