def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if (letter == i):
            continue
        else:
            answer += i
    return answer