n = int(input())
result = 1
answer = 0

for i in range(n, 0, -1):
    result *= i

result = str(result)

for i in range(len(result) -1 , -1, -1):
    if result[i] != '0':
        break
    answer += 1

print(answer)
