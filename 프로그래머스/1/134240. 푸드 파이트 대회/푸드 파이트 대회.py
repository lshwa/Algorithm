def solution(food):
    left = []
    for i in range(1, len(food)):
        left.append(str(i) * (food[i] // 2))
    left_str = ''.join(left)
    return left_str + '0' + left_str[::-1]