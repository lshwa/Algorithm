import sys, ast
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmds = input().strip()
    n = int(input())
    s = input().strip()
    dq = deque(ast.literal_eval(s))

    rev = False
    error = False

    for c in cmds:
        if c == 'R':
            rev = not rev

        elif c == 'D':
            if not dq:
                error = True
                break
            dq.pop() if rev else dq.popleft()


    if error:
        print('error')
    else:
        if rev:
            dq.reverse()
        print('[' + ','.join(map(str,dq)) + ']')


