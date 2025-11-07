def solution(str_list):
    answer = []
    
    target_l, target_r = 30, 30
    
    if 'l' in str_list:
        target_l = str_list.index('l')
    if 'r' in str_list:
        target_r = str_list.index('r')
    
    if target_l == 30 and target_r == 30:
        return []
    
    if target_l < target_r:
        return str_list[0:target_l]
    
    else:
        return str_list[target_r + 1:]