def solution(myString):
    result = ""
    for ch in myString:
        if ch == 'a' or ch == 'A':
            result += ch.upper()
        else:
            result += ch.lower()
    return result