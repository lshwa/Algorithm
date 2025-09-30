import sys
input = sys.stdin.readline

def adj(x: int) -> int:
    return x if x > 0 else x + 1  

N = int(input())
idx = 1 

for _ in range(N):
    a, b = map(int, input().split())
    idx += (adj(b) - adj(a))

print(idx if idx > 0 else idx - 1)