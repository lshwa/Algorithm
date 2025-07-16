import re

N = int(input())
numbers = []

for _ in range(N):
    line = input()
    found_numbers = re.findall(r'\d+', line)
    numbers.extend([int(num) for num in found_numbers])

numbers.sort()

for num in numbers:
    print(num)
