def solution(arr):
    
    idx = [i for i, v in enumerate(arr) if v == 2]
    if not idx:
        return [-1]
    return arr[idx[0]:idx[-1] + 1]