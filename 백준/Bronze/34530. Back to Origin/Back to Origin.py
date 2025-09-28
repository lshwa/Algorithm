import sys
input = sys.stdin.readline

d = int(input())
answer = 1
total = d 

while True:
    if total % 360 == 0:
        print(answer)
        break

    else:
        total += d
        answer += 1