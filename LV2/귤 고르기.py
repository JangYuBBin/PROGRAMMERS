# 귤 고르기

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!

from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    
    d = defaultdict(int)
    
    for t in tangerine:
        d[t] += 1
    
    arr = list()
    
    for key, value in d.items():
        arr.append((key, value))
    
    arr.sort(key = lambda x : x[1], reverse = True)
    
    for key, value in arr:
        k -= value
        if k < 0:
            k = 0
        answer += 1
        
        if k == 0:
            break
    
    return answer
