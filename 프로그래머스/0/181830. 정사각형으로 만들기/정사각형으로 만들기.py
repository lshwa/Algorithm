def solution(arr):
    n = len(arr)        # 행 개수
    m = len(arr[0])     # 열 개수 

    if n > m:
        for row in arr:
            row.extend([0] * (n - m))
    elif n < m:
        for _ in range(m - n):
            arr.append([0] * m)

    return arr