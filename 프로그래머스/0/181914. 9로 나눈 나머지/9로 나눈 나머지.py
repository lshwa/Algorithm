def solution(number):
    answer = 0
    for i in range(0, len(number), 1):
        answer += int(number[i])
    return answer % 9