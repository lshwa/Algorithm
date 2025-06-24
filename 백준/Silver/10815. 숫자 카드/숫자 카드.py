n = int(input())
cards = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for num in targets:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')