def solution(str_list, ex):
    answer = ''
    
    for item in str_list:
        if ex in item:
            continue
        else:
            answer += item
    
    return answer