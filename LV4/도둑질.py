# 도둑질 

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 처음 집을 털 것인가 털지 않을 것인가 두 가지 경우로 나누어서 생각해야 합니다..!!
# 3. 또한 dp[i]의 의미는 다음과 같습니다.
# 4. dp[i] : i번째 집까지 도달했을 때 얻을 수 있는 돈의 최댓값..!!
# 5. 약간 애매하게 풀었으므로 다음에 다시 풀어봐야 할 것 같습니다..!!

def solution(money):
    dp1 = [0] * len(money) # <<-- "처음 집을 선택하는 경우입니다..!!"
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, len(money), 1):
        if i == len(money) - 1:
            dp1[i] = max(dp1[i - 1], dp1[0])
        else:
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    dp2 = [0] * len(money) # <<-- "처음 집을 선택하지 않는 경우입니다..!!"
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, len(money), 1):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    
    max1 = max(dp1)
    max2 = max(dp2)

    answer = max(max1, max2)

    return answer
