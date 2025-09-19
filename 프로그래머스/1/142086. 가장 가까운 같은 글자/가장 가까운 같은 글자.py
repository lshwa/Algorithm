def solution(s):
    last_seen = {}
    answer = []
    
    for i, c in enumerate(s):
        if c in last_seen:
            answer.append(i - last_seen[c])
        else:
            answer.append(-1)
        last_seen[c] = i
    return answer