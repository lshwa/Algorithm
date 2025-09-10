def solution(arr):
    answer = []
    
    for item in arr:
        for i in range(item):
            answer.append(item)
    
    return answer