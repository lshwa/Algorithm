def solution(rank, attendance):
    available = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    available.sort()
    
    a, b, c = available[0][1], available[1][1], available[2][1]
    return 10000 * a + 100 * b + c
    
    
    