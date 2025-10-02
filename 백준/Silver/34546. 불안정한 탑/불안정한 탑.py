import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
answer = 0

target_height = min(tops)
for top in tops:
    answer += top - target_height

print(answer)