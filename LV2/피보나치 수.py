# 피보나치 수

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    if n < 2:
        return dp[n]
    else:
        pass
    
    for i in range(2, n + 1, 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1234567
    
    return dp[n]
