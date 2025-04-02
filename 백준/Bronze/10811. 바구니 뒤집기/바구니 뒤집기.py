n, m = map(int, input().split())

a = [i for i in range(1, n + 1)]

for i in range(m):
    i, j = map(int, input().split())
    temp = a[i-1:j]
    temp.reverse()
    a[i-1:j] = temp
    
for i in range(n):
    print(a[i], end = ' ')