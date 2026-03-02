def solution(name, yearning, photo):
    score = {n: y for n , y in zip(name, yearning)}
    answer = []
    
    for ppl in photo:
        total = 0
        for p in ppl:
            total += score.get(p, 0)
        answer.append(total)
    
    return answer 