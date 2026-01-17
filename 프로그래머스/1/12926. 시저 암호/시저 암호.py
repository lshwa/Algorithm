def solution(s, n):
    answer = ''
    
    for ch in s:
        if 'A' <= ch <= 'Z':
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += ch
        
    return answer