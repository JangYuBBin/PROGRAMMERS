# 소수 만들기

# my thoughts :
# 1. By using 조합 라이브러리, We can solve it..!!

from math import sqrt
from itertools import combinations

def IsPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num)) + 1, 1):
            if num % i == 0:
                return False
            
    return True

def solution(nums):
    answer = 0
    
    cases = list(combinations(nums, 3))
    
    for case in cases:
        if IsPrime(sum(case)):
            answer += 1
        else:
            pass
        
    return answer
