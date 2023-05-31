# 추억 점수

# my thoughts :
# 1. By using defaultdict, We can solve it..!!

from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    
    d = defaultdict(int)
    for n, y in zip(name, yearning):
        d[n] = y
    
    for p in photo:
        score = 0
        
        for c in p:
            if c not in d:
                continue
            else:
                score += d[c]
        
        answer.append(score)
        
    return answer
