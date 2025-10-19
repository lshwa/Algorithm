def solution(score):
    total_scores = [sum(s) for s in score]
    sorted_scores = sorted(total_scores, reverse = True)
    answer = [sorted_scores.index(s) + 1 for s in total_scores]
    
    return answer