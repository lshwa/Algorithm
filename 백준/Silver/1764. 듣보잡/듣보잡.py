import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_hearman = {input().strip() for _ in range(N)}
no_seeman = {input().strip() for _ in range(M)}

answer = sorted(no_hearman & no_seeman)

print(len(answer))
print("\n".join(answer))