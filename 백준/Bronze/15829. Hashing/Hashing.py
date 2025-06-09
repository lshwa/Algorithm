l = int(input())
letter = input()

r = 31
M = 1234567891
answer = 0

for i in range(l):
    num = ord(letter[i]) - ord('a') + 1
    answer += num * (r ** i)

answer %= M
print(answer)