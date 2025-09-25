def solution(n):
    pizza = 6
    answer = 1
    
    while True:
        if pizza % n == 0:
            return answer
        else:
            answer += 1
            pizza += 6
            
    