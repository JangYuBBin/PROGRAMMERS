# 점 찍기

from math import sqrt

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        val = int(sqrt(d**2 - x**2) / k)
        answer += val + 1
        
    return answer

print(solution(1, 5))
