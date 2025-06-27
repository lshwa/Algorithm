import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_to_num = {}
num_to_name = []

for i in range(1, N + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name.append(name)

answer = []

for _ in range(M):
    question = input().strip()
    if question.isdigit():
        answer.append(num_to_name[int(question) - 1])
    else:
        answer.append(str(name_to_num[question]))
    
print("\n".join(answer))

