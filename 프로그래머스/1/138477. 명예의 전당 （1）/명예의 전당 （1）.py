import heapq

def solution(k, score):
    hall = []
    answer = []
    
    for s in score:
        heapq.heappush(hall, s)
        if len(hall) > k:
            heapq.heappop(hall)
        answer.append(hall[0])
    
    return answer