import sys
input = sys.stdin.readline

N = int(input())
W = int(input())
answer = 0

if N == 5:
    answer += 50

if N <= 2:
    answer = N * 10
else:
    answer += (N * 10) + 20

if W > 1000:
    answer -= 15
    if answer < 0:
        answer = 0 

print(answer)