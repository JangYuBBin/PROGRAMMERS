# 숫자 블록

# my thoughts :
# 1. n번 숫자 블록에 깔리게 될 숫자는 n의 약수 중 2번째로 가장 큰 수입니다.
# 2. n의 약수 중에서 n을 제외한 10_000_000이하인 숫자를 모두 구한 후 그 중에서 가장 큰 수를 return 해주면 될 것입니다..!!
# 3. 중요한 문제이고 틀린 문제이므로 나중에 다시 풀어보도록 합시다..!!

from math import sqrt

def solution(begin, end):
    answer = []
    
    def function(num): # <<-- "num번 블록에서 설치될 블록을 찾아주는 함수입니다..!!"
        if num == 1:
            return 0
        else:
            pass
        
        arr = list() # <<-- "num을 제외한 num의 약수를 모두 담을 1차원 리스트의 선언입니다..!!"
        arr.append(1)
        
        for i in range(2, int(sqrt(num)) + 1, 1):
            if num % i == 0:
                if i <= 10_000_000:
                    arr.append(i)
                else:
                    pass
                
                if num // i <= 10_000_000:
                    arr.append(num // i)
                else:
                    pass
        
        return max(arr)
    
    for num in range(begin, end + 1, 1):
        answer.append(function(num))
    
    return answer
