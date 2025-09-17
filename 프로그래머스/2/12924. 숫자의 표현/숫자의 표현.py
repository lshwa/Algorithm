def solution(n):
    answer = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 1:
                answer += 1
            j = n // i
            if j != i and j % 2 == 1:
                answer += 1
        i += 1
    
    return answer