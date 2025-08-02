def solution(num_list):
    product = 1
    total = 0

    for num in num_list:
        product *= num
        total += num

    if product < total ** 2:
        return 1
    else:
        return 0