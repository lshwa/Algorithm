def solution(n):
    sqrt = []
    for i in range(1, 1001):
        sqrt.append(i * i)
    if n in sqrt:
        return 1
    else:
        return 2