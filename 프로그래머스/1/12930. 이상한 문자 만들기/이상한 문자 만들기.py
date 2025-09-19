def solution(s):
    answer = []
    for word in s.split(" "):          
        temp = ""
        for i, ch in enumerate(word):
            if i % 2 == 0:
                temp += ch.upper()
            else:
                temp += ch.lower()
        answer.append(temp)
    return " ".join(answer)