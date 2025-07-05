import sys
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

a = b = -1
cnt_a = 0
cur = ans = 0

for x in fruits:
    if x == a or x == b:
        cur += 1
    else:
        cur = cnt_a + 1
    
    if x == a:
        cnt_a += 1
    else:
        cnt_a = 1
        b = a
        a = x 
    
    ans = max(ans, cur)

print(ans)