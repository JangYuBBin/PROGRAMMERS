# 콜라 문제

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        q, r = divmod(n, a)
        answer += b * q
        n -= a * q
        n += b * q
        
    return answer

print(solution(2, 1, 20))
