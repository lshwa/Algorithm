def solution(myString, pat):
    answer = 0
    my_string_modify = ''
    
    for str in myString:
        if str == 'A':
            my_string_modify += 'B'
        elif str == 'B':
            my_string_modify += 'A'
        else:
            my_string_modify += str
    
    if pat in my_string_modify:
        answer = 1
    
    return answer