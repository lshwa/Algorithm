def solution(emergency):
    ranking = {
        value : rank + 1
        for rank, value in enumerate(sorted(emergency, reverse=True))
    }
    
    result = [ranking[value] for value in emergency]
    return result

