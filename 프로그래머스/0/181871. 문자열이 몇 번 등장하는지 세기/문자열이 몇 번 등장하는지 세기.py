def solution(myString, pat):
    answer = 0
    word_len = len(pat)
        
    for i in range(0, len(myString) - word_len + 1):
        if myString[i:i+ word_len] == pat:
            answer += 1
    
    return answer