def solution(my_string):
    total = 0
    num = ''  

    for ch in my_string:
        if ch.isdigit():
            num += ch  
        else:
            if num:  
                total += int(num)
                num = ''  
    if num:
        total += int(num)
    
    return total