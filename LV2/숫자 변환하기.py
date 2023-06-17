# 숫자 변환하기

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

def solution(x, y, n):
    answer = 0
    
    dp = [float("inf")] * 1_000_001
    dp[x] = 0
    
    for i in range(x + 1, y + 1, 1):
        if i - n >= x:
            dp[i] = min(dp[i], dp[i - n] + 1)
        
        if i % 2 == 0 and i // 2 >= x:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        if i % 3 == 0 and i // 3 >= x:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    if dp[y] == float("inf"):
        return -1
    else:
        return dp[y]
