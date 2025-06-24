def solution(myString):
    answer = []
    temp = 0
    for s in myString:
        if s == 'x':
            answer.append(temp)
            temp = 0
        else:
            temp += 1
    
    answer.append(temp)
    return answer