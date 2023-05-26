# 의상

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!
# 2. 또한 약간의 수학적 사고력을 요하는 문제였던 것 같습니다..!!

from collections import defaultdict

def solution(clothes):
    answer = 1
    
    d = defaultdict(int)
    
    for name, sort in clothes:
        d[sort] += 1
    
    for k, v in d.items():
        answer *= (v + 1)
    
    answer -= 1 # <<-- "아무것도 입지 않은 상태를 빼줘야 하기 때문입니다..!!"
    
    return answer
