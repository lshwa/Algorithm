def solution(s):
    answer = True
    cnt_p = 0
    cnt_y = 0
    
    for ch in s:
        if ch == 'p' or ch == 'P':
            cnt_p += 1
        elif ch == 'y' or ch == 'Y':
            cnt_y += 1
    
    if cnt_p != cnt_y:
        return False


    return True