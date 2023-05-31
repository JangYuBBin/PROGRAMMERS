# 소수 찾기

from math import sqrt

def IsPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num)) + 1, 1):
            if num % i == 0:
                return False
    
    return True

def solution(n):
    answer = 0
    
    for i in range(1, n + 1, 1):
        if IsPrime(i):
            answer += 1
    
    return answer
