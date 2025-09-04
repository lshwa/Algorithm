def solution(arr):
    answer = []
    prev = None
    for x in arr:
        if x != prev:
            answer.append(x)
            prev = x
    return answer