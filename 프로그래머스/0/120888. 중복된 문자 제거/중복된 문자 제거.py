def solution(my_string):
    answer = ''
    hist = []
    
    for i in range(len(my_string)):
        if my_string[i] in hist:
            continue
        else:
            answer += my_string[i]
            hist.append(my_string[i])
    
    return answer