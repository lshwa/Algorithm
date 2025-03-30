h, m = map(int, input().split())

if (m >= 45):
    print(h, m - 45)
    
else:
    if(h != 0):
        h -= 1
        m = m + 15
        print(h, m)
        
    else:
        h = 23
        m = m + 15
        print(h, m)