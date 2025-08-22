def solution(n):
    cnt_one = bin(n).count("1")
    x = n + 1
    while bin(x).count("1") != cnt_one:
        x += 1
    return x
    
    
    