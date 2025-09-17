def solution(s):
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    for ch in s:
        if not ch.isdigit():
            return False
    
    return True