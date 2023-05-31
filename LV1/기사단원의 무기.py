# 기사단원의 무기

from math import sqrt

def count(num):
    answer = 0
    
    for i in range(1, int(sqrt(num)) + 1, 1):
        if num % i == 0:
            j = num // i
            
            if i == j:
                answer += 1
            else:
                answer += 2
    
    return answer

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1, 1):
        if count(i) > limit:
            answer += power
        else:
            answer += count(i)

    return answer

print(solution(5, 3, 2))
