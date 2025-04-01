x, y , w, h = map(int,input().split())

if (1 <= w <= 1000) and (1 <= h <= 1000) is False:
    print("Retry")
if (x == 0) or (y == 0) or (x == w) or (y == h):
    print(0)
else:
    goWidth = min(w - x, x)
    goHeight = min(h -y , y)
    print(min(goWidth, goHeight))