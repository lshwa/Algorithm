def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2 + 1, 1):
        num = numbers[i]
        answer.append(num)
    return answer