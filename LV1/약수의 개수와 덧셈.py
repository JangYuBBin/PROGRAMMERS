# 약수의 개수와 덧셈

from math import sqrt

def count(num):
    answer = 0
    
    if num == 1:
        return 1
    else:
        pass
    
    for i in range(1, int(sqrt(num)) + 1, 1):
        if num % i == 0:
            j = num // i
            
            if i == j:
                answer += 1
            else:
                answer += 2
    
    return answer
            
                
    

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1, 1):
        if count(i) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
