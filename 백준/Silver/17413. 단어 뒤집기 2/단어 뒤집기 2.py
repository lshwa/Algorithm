import sys
s = sys.stdin.readline().rstrip()

res = []
word = []
in_tag = False

for ch in s:
    if in_tag:
        res.append(ch)
        if ch == '>':
            in_tag = False
    
    else:
        if ch == '<':
            if word:
                res.extend(reversed(word))
                word.clear()
            res.append(ch)
            in_tag = True
        
        elif ch == ' ':
            res.extend(reversed(word))
            word.clear()
            res.append(' ')
        else:
            word.append(ch)

if word:
    res.extend(reversed(word))

print(''.join(res))