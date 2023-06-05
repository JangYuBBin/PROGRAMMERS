# 피로도 

# my thoughts :
# 1. By using Brute Force, We can solve it..!!
# 2. 문제에서 dungeons의 세로 행의 길이 는 1 이상 8 이하라고 하였으므로 저는 순열 라이브러리를 활용하여 모든 경우를 구한 뒤 정답을 구하겠습니다..!!

from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    cases = list(permutations(dungeons, len(dungeons)))
    
    for case in cases:
        cnt = 0
        temp_k = k
        
        for need, use in case:
            if temp_k >= need:
                temp_k -= use # <<-- ""최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다."
                cnt += 1
            else:
                break
        
        answer.append(cnt)
    
    answer.sort(reverse = True)
    
    return answer[0]
