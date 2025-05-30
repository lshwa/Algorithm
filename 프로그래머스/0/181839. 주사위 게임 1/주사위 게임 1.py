def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:  # 둘 다 홀수
        return a**2 + b**2
    elif a % 2 == 0 and b % 2 == 0:  # 둘 다 짝수
        return abs(a - b)
    else:  # 하나만 홀수
        return 2 * (a + b)