def solution(s):
    cnt_trans, cnt_zero = 0, 0
    
    while s != '1':
        cnt_trans += 1
        zero = s.count('0')
        
        cnt_zero += zero
        s = s.replace('0', '')
        s = bin(len(s))[2:]
    
    return [cnt_trans, cnt_zero]