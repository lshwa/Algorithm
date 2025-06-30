import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
conference = [tuple(map(int, input().split())) for _ in range(N)]

conference.sort(key = lambda x: (x[1], x[0]))
current_end = -1

for start, end in conference:
    if start >= current_end:
        cnt += 1
        current_end = end

print(cnt)