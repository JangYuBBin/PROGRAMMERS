# 예산

from collections import deque

def solution(d, budget):
    answer = 0
    
    d.sort()
    d = deque(d)
    
    while d:
        num = d.popleft()
        
        if num <= budget:
            budget -= num
            answer += 1
        else:
            break
        
    return answer
