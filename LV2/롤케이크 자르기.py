# 롤케이크 자르기

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!

def solution(topping):
    answer = 0
    
    d1 = dict()
    for t in topping:
        if t not in d1:
            d1[t] = 1
        else:
            d1[t] += 1
    
    d2 = dict()
    for t in topping:
        if t not in d2:
            d2[t] = 1
        else:
            d2[t] += 1
        
        d1[t] -= 1
        if d1[t] == 0:
            del d1[t]
        
        if len(d1.keys()) == len(d2.keys()):
            answer += 1
        else:
            pass
    
    return answer
