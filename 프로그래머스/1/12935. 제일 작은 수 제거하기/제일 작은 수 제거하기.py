def solution(arr):
    answer = []
    min_num = min(arr)
    
    for i in range(0, len(arr)):
        if arr[i] == min_num:
            continue
        else:
            answer.append(arr[i])
    
    if len(answer) == 0:
        return [-1]
    else:
        return answer