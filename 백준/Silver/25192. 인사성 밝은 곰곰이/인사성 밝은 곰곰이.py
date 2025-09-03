import sys
input = sys.stdin.readline

n = int(input().strip())
seen = set()
answer = 0

for _ in range(n):
    s = input().strip()
    if s == "ENTER":
        answer += len(seen)
        seen.clear()
    else:
        seen.add(s)

answer += len(seen)
print(answer)