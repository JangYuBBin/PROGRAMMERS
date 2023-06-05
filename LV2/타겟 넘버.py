# 타겟 넘버

# my thoughts :
# 1. By using DFS and BackTracking, We can solve it..!!

import sys
sys.setrecursionlimit(10**6) # <<-- "재귀의 최대 깊이 초과 판정을 피하기 위한 선언입니다..!!"

def solution(numbers, target):
    global answer
    answer = 0
    
    result = [] 
    
    def dfs():
        global answer
        
        if len(result) == len(numbers):
            if sum(result) == target:
                answer += 1
            else:
                pass
            return
        else:
            result.append(numbers[len(result)])
            dfs()
            result.pop()
            
            result.append(-1 * numbers[len(result)])
            dfs()
            result.pop()
    
    dfs()
    
    return answer
