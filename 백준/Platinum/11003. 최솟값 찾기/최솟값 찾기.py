import sys
from collections import deque

read  = sys.stdin.buffer.readline
write = sys.stdout.buffer.write    

N, L = map(int, read().split())
nums  = map(int, read().split())   

dq   = deque()
buf  = bytearray()                 
BULK = 100_000                     

for i, x in enumerate(nums):
    while dq and dq[-1][0] >= x:
        dq.pop()

    dq.append((x, i))

    if dq[0][1] <= i - L:
        dq.popleft()

    buf.extend(f"{dq[0][0]} ".encode())

    if (i + 1) % BULK == 0:
        write(buf)
        buf.clear()

if buf:
    write(buf)