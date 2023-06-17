# 최고의 집합

# my thoughts :
# 1. 가끔은 감으로 풀어야 할때도 있습니다..!!

def solution(n, s):
    answer = []
    
    while n != 0:
        q, r = divmod(s, n)
        if q == 0:
            return [-1]
        
        answer.append(q)
        
        s -= q
        
        n -= 1
        
    answer.sort(reverse = False)
    
    return answer
