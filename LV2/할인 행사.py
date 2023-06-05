# 할인 행사

# my thoughts :
# 1. By using Brute Force, We can solve it..!!

from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    d = dict()
    for w, n in zip(want, number):
        d[w] = n
    
    for i in range(0, len(discount), 1):
        if i + 10 - 1 >= len(discount):
            break
        else:
            pass
        
        temp = discount[i:i + 10:1]
        
        temp_d = defaultdict(int)
        
        for t in temp:
            temp_d[t] += 1
            
        checkFlag = True
        
        for k in d.keys():
            if d[k] > temp_d[k]:
                checkFlag = False
                break
            else:
                pass
            
        if checkFlag == True:
            answer += 1
        else:
            pass    
        
    return answer
