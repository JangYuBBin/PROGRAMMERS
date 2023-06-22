# 거스름돈 # -->> "틀린 문제이므로 나중에 다시 풀어보도록 합시다..!!"

# another solution
# 풀이참조출처 : "https://yejin72.tistory.com/35"

# another thoughts :
#       1   2   3   4   5   6   7   8   9   10
# 1     1   1   1   1   1   1   1   1   1   1
# 2     0   1   1   2   2   3   3   4   4   5
# 5     0   0   0   0   1   1   2   2   3   4

def solution(n, money):
    answer = 0

    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for i in range(m, n + 1, 1):
            dp[i] += dp[i - m]
            dp[i] %= 1_000_000_007
    
    return dp[n]

print(solution(5, [1, 2, 5]))
