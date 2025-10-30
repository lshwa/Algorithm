def solution(triangle):
    n = len(triangle)
    dp = triangle[-1] 
    
    for i in range(n - 2, -1, -1):
        new_dp = []
        for j in range(len(triangle[i])):
            new_dp.append(triangle[i][j] + max(dp[j], dp[j + 1]))
        dp = new_dp
    
    return dp[0]