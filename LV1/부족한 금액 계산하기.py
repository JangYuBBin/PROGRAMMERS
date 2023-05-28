# 부족한 금액 계산하기

def solution(price, money, count):
    cost = sum(price * i for i in range(1, count + 1, 1))
    
    if cost <= money:
        return 0
    else:
        return cost - money
