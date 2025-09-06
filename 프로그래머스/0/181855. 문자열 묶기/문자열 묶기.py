from collections import Counter

def solution(strArr):
    lengths_counts = Counter(map(len, strArr))
    return max(lengths_counts.values())
