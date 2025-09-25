def solution(myString):
    
    answer = ''
    for i in range(0, len(myString)):
        if str(myString[i]) <= 'l':
            answer += 'l'
        else:
            answer += str(myString[i])
        
        
    return answer