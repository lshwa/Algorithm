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
            out.append(str(heappop(heap)[1]))
        else:
            out.append('0')
    else:
        heappush(heap, (abs(cmd), cmd))

sys.stdout.write("\n".join(out))
