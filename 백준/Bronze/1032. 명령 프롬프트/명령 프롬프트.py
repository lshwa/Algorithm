
n = int(input())

f = list(input())
f_len = len(f)

for i in range(n - 1):
    o = list(input())
    for j in range(f_len):
        if f[j] != o[j]:
            f[j] = '?'

print(''.join(f))