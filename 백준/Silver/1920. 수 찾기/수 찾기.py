import sys
input = sys.stdin.readline

N = int(input())
N_set = set(map(int, input().split()))

M = int(input())
question = map(int, input().split())

out = []
for num in question:
    out.append("1" if num in N_set else "0")

print("\n".join(out))
