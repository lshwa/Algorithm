import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split()) 
cnt = answer = 0

for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            answer = i
            break  

print(answer)