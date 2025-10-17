def solution(s):
    sorted_chars = sorted(s, reverse = True)
    return ''.join(sorted_chars)
