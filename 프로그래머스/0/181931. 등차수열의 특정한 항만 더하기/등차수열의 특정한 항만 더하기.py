def solution(a, d, included):
    ans = 0
    for i, inc in enumerate(included): 
        if inc:
            ans += a + d*i
    return ans