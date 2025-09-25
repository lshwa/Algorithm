def solution(arr):
    
    n = len(arr)
    m = len(arr[0])
    
    if n != m:
        return 0
    
    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
