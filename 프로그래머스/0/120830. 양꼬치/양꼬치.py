def solution(n, k):
    free = 0
    if (n >= 10):
        free += (n // 10)
        
    answer = (n * 12000) + ((k - free) * 2000)
    return answer