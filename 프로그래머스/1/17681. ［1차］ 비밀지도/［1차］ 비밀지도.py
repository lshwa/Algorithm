def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        merged = a | b
        binary = format(merged, f'0{n}b')
        
        row = binary.replace('1','#').replace('0',' ')
        answer.append(row)
    
    return answer