def rev(x):
    x_str = str(x)
    reversed_str = x_str[::-1]
    reversed_int = int(reversed_str)
    return reversed_int

x, y = map(int, input().split())
answer = rev(rev(x) + rev(y))
print(answer)


