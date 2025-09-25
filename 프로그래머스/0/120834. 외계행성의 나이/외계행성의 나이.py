def solution(age):
    answer = ''
    mapping = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    age = str(age)
    
    for i in range(len(age)):
        answer += mapping[int(age[i])]
   
    return answer