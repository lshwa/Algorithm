def solution(my_string):
    parts = my_string.split()
    result = int(parts[0])
    
    for i in range(1, len(parts),2):
        op = parts[i]
        num = int(parts[i + 1])
        
        if op == '+':
            result += num
        else:
            result -= num
    
    return result

