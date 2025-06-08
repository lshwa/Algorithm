n = int(input())

while n >= 4:
    flag = True
    for ch in str(n):
        if ch not in '47':
            flag = False
            break
    if flag:
        print(n)
        break
    n -= 1
