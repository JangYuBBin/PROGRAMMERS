# 숫자 짝꿍

from collections import defaultdict

def solution(X, Y):
    answer = ""
    
    d_X = defaultdict(int)
    d_Y = defaultdict(int)
    
    for c in X:
        d_X[c] += 1
    
    for c in Y:
        d_Y[c] += 1
        
    d = dict()
    
    for num in ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]:
        val = min(d_X[num], d_Y[num])
        
        if val == 0:
            continue
        else:
            d[num] = val
    
    for num in ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]:
        if num not in d:
            continue
        else:
            answer += num * d[num]
            
    if not answer:
        return "-1"
    elif answer == "0" * len(answer):
        return "0"
    else:
        return answer

print(solution("100", "2345"))
