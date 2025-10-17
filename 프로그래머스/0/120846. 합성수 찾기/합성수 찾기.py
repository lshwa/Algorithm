def solution(n):
    def count_divisors(num):
        count = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                count += 2 if i != num // i else 1
        return count

    answer = 0
    for x in range(1, n + 1):
        if count_divisors(x) >= 3:  
            answer += 1
    return answer