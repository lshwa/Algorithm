isbn = input().strip()

weights = [1, 3] * 6 + [1]
missing_index = isbn.index('*')
total = 0

for i, ch in enumerate(isbn):
    if ch == '*':
        continue
    total += int(ch) * weights[i]

for digit in range(10):
    check_sum = total + digit * weights[missing_index]
    if check_sum % 10 == 0:
        print(digit)
        break

