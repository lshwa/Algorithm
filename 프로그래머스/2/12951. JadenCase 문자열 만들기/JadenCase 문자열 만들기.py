def solution(s):
    s = s.lower()  
    answer = ''
    flag = True   

    for ch in s:
        if flag and ch.isalpha():  
            answer += ch.upper()
            flag = False
        else:
            answer += ch
            if ch == ' ':
                flag = True 
            else:
                flag = False
    return answer