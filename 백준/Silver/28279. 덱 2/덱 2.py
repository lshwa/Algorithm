from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
deck = deque()
out = [] # 정보들을 모아놨다가 한번에 출력

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "1":
        deck.appendleft(cmd[1])
    
    elif cmd[0] == "2":
        deck.append(cmd[1])

    elif cmd[0] == "3":
        if len(deck) == 0:
            out.append(-1)
        else:
            out.append(deck.popleft())
    
    elif cmd[0] == "4":
        if len(deck) == 0:
            out.append(-1)
        else:
            out.append(deck.pop())

    elif cmd[0] == "5":
        out.append(len(deck))
    
    elif cmd[0] == "6":
        if len(deck) == 0:
            out.append(1) 
        else:
            out.append(0)
    
    elif cmd[0] == "7":
        if len(deck) == 0:
            out.append(-1)
        else:
            out.append(deck[0])
    
    elif cmd[0] == "8":
        if len(deck) == 0:
            out.append(-1)
        else:
            out.append(deck[-1])

print("\n".join(map(str, out)))