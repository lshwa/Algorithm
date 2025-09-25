def solution(arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2):
        row_sum = []
        for a, b in zip(row1, row2):
            row_sum.append(a + b)
        answer.append(row_sum)
    
    return answer