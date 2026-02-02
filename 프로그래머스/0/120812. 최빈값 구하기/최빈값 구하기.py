from collections import Counter

def solution(array):
    counter = Counter(array)
    max_count = max(counter.values())
    
    modes = [num for num, cnt in counter.items() if cnt == max_count]
    
    return modes[0] if len(modes) == 1 else -1