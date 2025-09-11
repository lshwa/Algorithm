def solution(a, b, c):
    answer = 0
    len_dice = len({a, b, c})
    
    if len_dice == 3:
        answer = a + b +c
    elif len_dice == 2:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    
    return answer