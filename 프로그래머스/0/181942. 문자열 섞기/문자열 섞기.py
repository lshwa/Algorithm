def solution(str1, str2):
    answer = ''
    
    target = min(len(str1), len(str2))
    for i in range(0, target):
        answer += str1[i]
        answer += str2[i]
    
    return answer