def is_hansu(x):
    if x < 100:
        return True
    digits = list(map(int, str(x)))
    diff = digits[1] - digits[0]

    for i in range(1, len(digits)):
        if digits[i] - digits[i - 1] != diff:
            return False
    return True

n = int(input())
count = 0
for i in range(1, n + 1):
    if is_hansu(i):
        count += 1
print(count)
                   
