import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
stack = []
current = 1

for student in students:
    while stack and stack[-1] == current:
        stack.pop()
        current += 1
    if student == current:
        current += 1
    else:
        stack.append(student)

while stack and stack[-1] == current:
    stack.pop()
    current += 1

print("Nice" if not stack else "Sad")