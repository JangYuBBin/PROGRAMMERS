# 숫자 카드 나누기

# my thoughts :
# 1. 왠지 이 문제는 최대공약수와 관련 있는 문제라는 내 추측의 정당성을 어떻게 확인할 것인가?
# 2. 만약 arrayA의 모든 수를 나눌 수 있는 수가 1, 2, 3, 6이라고 가정해보자.
# 3. 만약 6이 정답이 아니라면 1, 2, 3 중 하나가 정답이 되어야 할 것이다.
# 4. 그러나 6이 정답이 아니라는 뜻은 arrayB의 수 중 적어도 하나 이상이 6으로 나누어 떨어진다는 뜻이고 이는 3으로도 나누어 떨어진다는 뜻이다. 따라서 이 경우에는 조건 1을 만족하는 양의 정수가 존재하지 않는다는 뜻이다. 
# 5. 따라서 arrayA의 최대공약수만 확인하면 된다는 뜻이고 
# 6. 이는 최대공약수만 확인해도 된다는 정당성을 증명한 것이다..!!

from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    # 먼저 조건 1을 만족하는 양의 정수 a가 존재하는지 확인해보자
    checkFlag1 = True
    
    a1 = arrayA[0]
    
    for i in range(1, len(arrayA), 1):
        a1 = gcd(a1, arrayA[i])
    
    if a1 == 1:
        checkFlag1 = False
    else:
        for i in range(0, len(arrayB), 1):
            if arrayB[i] % a1 == 0:
                checkFlag1 = False
                break
    
    # 그다음으로 조건 2을 만족하는 양의 정수 a가 존재하는지 확인해보자
    checkFlag2 = True
    
    a2 = arrayB[0]
    
    for i in range(1, len(arrayB), 1):
        a2 = gcd(a2, arrayB[i])
    
    if a2 == 1:
        checkFlag2 = False
    else:
        for i in range(0, len(arrayA), 1):
            if arrayA[i] % a2 == 0:
                checkFlag2 = False
                break
    
    if not checkFlag1 and not checkFlag2:
        return 0
    elif checkFlag1 and not checkFlag2:
        return a1
    elif checkFlag2 and not checkFlag1:
        return a2
    else:
        return max(a1, a2)
        
    return answer
