import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
heap = [] 
out = []

for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if heap:
            out.append(str(-heappop(heap)))
        else:
            out.append('0')
    else:
        heappush(heap, -cmd)

sys.stdout.write("\n".join(out))
