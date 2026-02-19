def solution(a, b, n):
    answer = 0
    
    while n >= a:
        exchanged = n // a
        gained = exchanged * b
        answer += gained
        n = (n % a) + gained
        
    return answer