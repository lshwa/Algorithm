def solution(arr):
    answer = []
    
    for i in range(11):
        if len(arr) <= 2 ** i:
            target_len = 2**i
            break
    
    for i in range(target_len - len(arr)):
        arr.append(0)
    
    return arr