import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end  = max(lines)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in lines)
    
    if count >= N:
        answer = mid
        start = mid + 1
    
    else:
        end = mid - 1

print(answer)
