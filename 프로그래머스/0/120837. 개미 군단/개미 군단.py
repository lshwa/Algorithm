def solution(hp):
    answer = 0
    for attack in [5, 3, 1]:
        answer += hp // attack
        hp %= attack
        
        
    return answer