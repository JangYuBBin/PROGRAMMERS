# 줄 서는 방법

# my thoughts :
# 1. 20!의 값은 비약적으로 큰 수입니다. 따라서 우리는 백트래킹을 활용하여 문제를 풀 수 없습니다.
# 2. 따라서 우리는 다른 방법을 생각해내야 합니다.
# 3. ....
# 4. ....

from math import factorial

def solution(n, k):
    answer = []
    
    arr = list(range(1, n + 1, 1))
    
    while True:
        n -= 1
        q, r = divmod(k, factorial(n))
        
        if r == 0:
            answer.append(arr.pop(q - 1))
            break
        else:
            answer.append(arr.pop(q))
            k = r
    
    while arr:
        answer.append(arr.pop())
        
    return answer

print(solution(3, 5))
