def solution(n, control):
    answer = 0
    num = len(control)
    for i in range(0, num, 1):
        if (control[i] == 'w'):
            n += 1
        elif (control[i] == 's'):
            n -= 1
        elif (control[i] == 'd'):
            n += 10
        elif (control[i] == 'a'):
            n -= 10
    
    return n