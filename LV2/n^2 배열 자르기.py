# n^2 배열 자르기

# my thoughts :
# 1. 약간의 수학적 사고력이 필요한 문제였습니다..!!

def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1, 1):
        q, r = divmod(i, n)
        
        answer.append(max(q, r) + 1)
    return answer
