def solution(myStr):
    for ch in ['a', 'b', 'c']:
        myStr = myStr.replace(ch, ' ')
        
    parts = []
    for s in myStr.split(' '):
        if s != '':
            parts.append(s)
    if parts:
        return parts
    else:
        return ["EMPTY"]
    
    

