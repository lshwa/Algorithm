def solution(arr):
    answer = []
    
    for list in arr:
        if list >= 50 and list % 2 == 0:
            answer.append(list // 2)
        elif list < 50 and list % 2 == 1:
            answer.append(list * 2)
        else:
            answer.append(list)
    
    return answer