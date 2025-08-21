def solution(s):
    answer = True
    cnt = 0
    
    for str in s:
        if cnt == 0 and str == ')':
            return False
        elif str == '(':
            cnt += 1
        elif str == ')':
            cnt -= 1
    
    return cnt == 0