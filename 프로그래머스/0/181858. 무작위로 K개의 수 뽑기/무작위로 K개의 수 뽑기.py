def solution(arr, k):
    answer = []
    
    for item in arr:
        if item not in answer:
            answer.append(item)
        
        if len(answer) == k:
            break
    
    while len(answer) < k:
        answer.append(-1)
    
    return answer