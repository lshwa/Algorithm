def star(n):
    if n == 1:
        return ["*"]

    prev = star(n // 3)
    res = []

    for line in prev:
        res.append(line * 3)
        
    for line in prev:
        res.append(line + " " * (n // 3) + line)
    
    for line in prev:
        res.append(line * 3)
    
    return res 

N = int(input())
print("\n".join(star(N)))