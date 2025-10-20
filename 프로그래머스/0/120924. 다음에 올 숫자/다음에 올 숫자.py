def solution(common):
    answer = 0
    
    a, b, c = common[0], common[1], common[2]
    
    if (b - a) == (c - b):
        d = b - a
        return common[-1] + d
    
    else:
        r = b // a
        return common[-1] * r