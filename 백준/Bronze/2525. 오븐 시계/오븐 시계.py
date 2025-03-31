a, b = map(int,input().split())
c = int(input())
minute = 0

if (b + c < 60):
    print(a, b+c, end = ' ')

else: 
    h = (b + c) // 60
    if (a + h >= 24):
        a = a + h - 24 
        minute = b + c - (60 * h)
        print(a, minute, end = ' ')
    
    else:
        a += h
        minute = b + c - (60 * h)
        print(a, minute, end = ' ')
        