import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_password = dict(input().split() for _ in range(N))

answer = [] 
for _ in range(M):
    site = input().strip()
    answer.append(site_password[site])

print("\n".join(answer))