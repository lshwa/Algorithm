def solution(array, commands):
    answer = []
    for cmd in commands:
        copy = array[cmd[0] - 1: cmd[1]]
        copy.sort()
        answer.append(copy[cmd[2] - 1])
    return answer