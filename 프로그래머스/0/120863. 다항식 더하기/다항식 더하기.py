def solution(polynomial):
    coef_x = 0
    const = 0
    
    for term in polynomial.split(" + "):
        if 'x' in term:
            if term == 'x':
                coef_x += 1
            else:
                coef_x += int(term.replace('x',''))
        else:
            const += int(term)
    
    parts = []
    if coef_x:
        if coef_x == 1:
            parts.append("x")
        else:
            parts.append(f"{coef_x}x")
    
    if const:
        parts.append(str(const))
    
    return " + ".join(parts)
                