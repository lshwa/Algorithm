def solution(myString, pat):
    for end in range(len(myString), 0, -1):
        if myString[:end].endswith(pat):
            return myString[:end]
