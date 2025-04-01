n = int(input())
te = list(map(int, input().split()))
y = m = 0

for n in te:
    y += (n // 30 + 1) * 10
    m += (n // 60 + 1) * 15
    
if m == y:
    print("Y M", m)

elif m > y:
    print("Y", y)

else:
    print("M", m)