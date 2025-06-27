import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
S = set()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        S.add(int(cmd[1]))

    elif op == "remove":
        S.discard(int(cmd[1]))          # 없는 원소일 때 예외 없음

    elif op == "check":
        write("1\n" if int(cmd[1]) in S else "0\n")

    elif op == "toggle":
        x = int(cmd[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif op == "all":
        S = set(range(1, 21))
        
    elif op == "empty":
        S.clear()