# 약수의 합

from math import sqrt

def solution(n):
    answer = 0
    
    if n == 1:
        return 1
    else:
        pass
    
    for i in range(1, int(sqrt(n)) + 1, 1):
        if n % i == 0:
            a = i
            b = n // i
            
            if a != b:
                answer += a + b
            else:
                answer += a
    
    return answer
