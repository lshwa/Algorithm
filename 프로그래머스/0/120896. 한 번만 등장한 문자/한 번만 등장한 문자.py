def solution(s):
    answer = ''
    
    for ch in sorted(set(s)):
        if s.count(ch) == 1:
            answer += ch
            
    return answer