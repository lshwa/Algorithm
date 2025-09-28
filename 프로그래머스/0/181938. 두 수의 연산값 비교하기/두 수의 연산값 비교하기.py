def solution(a, b):
    score_1 = int(str(a) + str(b))
    score_2 = 2 * a * b
    
    if score_1 >= score_2:
        return score_1
    else:
        return score_2
