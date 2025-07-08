import sys
input = sys.stdin.readline

N = int(input())
log = set()

for _ in range(N):
    name, cmd = input().split()
    if cmd == 'enter':
        log.add(name)
    
    if cmd == 'leave':
        log.remove(name)

for name in sorted(log, reverse = True):
    print(name)