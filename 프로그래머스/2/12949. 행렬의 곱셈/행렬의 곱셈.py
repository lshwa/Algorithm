def solution(arr1, arr2):
    n, k, m = len(arr1), len(arr1[0]), len(arr2[0])
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            s = 0
            for t in range(k):
                s += arr1[i][t] * arr2[t][j]
            result[i][j] = s

    return result