# 2 x n 타일링

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

def solution(n):
    answer = 0
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1, 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1_000_000_007
    
    answer = dp[n]
    
    return answer
