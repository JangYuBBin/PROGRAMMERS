# 멀리 뛰기 

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1, 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        
        dp[i] %= 1234567
    
    return dp[n]
