# 소수 찾기2

# my thoughts :
# 1. By using Brute Force, We can solve it..!!
# 2. 순열 라이브러리를 활용할 것..!!

from itertools import permutations
from math import sqrt

def IsPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num)) + 1, 1):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    answer = 0
    
    numbers = list(numbers)
    
    cases = list()
    for i in range(1, len(numbers) + 1, 1):
        cases.extend(list(permutations(numbers, i)))
    cases = ["".join(case) for case in cases]
    cases = list(map(int, cases))
    cases = list(set(cases))
    
    print(cases)
    
    for case in cases:
        if IsPrime(case):
            answer += 1
        
    return answer
