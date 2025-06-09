n = int(input())
arr = []

for i in range(0, n, 1):
    s = input()
    arr.append(s)

arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))

for word in arr:
    print(word)