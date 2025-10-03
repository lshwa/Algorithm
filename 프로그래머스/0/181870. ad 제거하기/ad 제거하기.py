def solution(strArr):
    answer = []
    for item in strArr:
        if "ad" in item:  
            continue
        else:
            answer.append(item)
    return answer