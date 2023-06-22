# 메뉴 리뉴얼

# my thoughts :
# 1. 조합 라이브러리를 활용하여 문제에 접근해봅시다..!!

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    d1 = defaultdict(int)
    
    for order in orders:
        order = list(order)
        
        cases = list()
        
        for i in course:
            temp = list(combinations(order, i))
            
            for i in range(0, len(temp)):
                temp[i] = list(temp[i])
                temp[i].sort()
                temp[i] = "".join(temp[i])
            
            cases.extend(temp)
        
        for case in cases:
            d1[case] += 1

    d2 = defaultdict(list)
    
    for k in d1.keys():
        d2[len(k)].append((k, d1[k]))
    
    for k in d2.keys():
        d2[k].sort(key = lambda x : x[1], reverse = True)
        
    for i in course:
        for key, val in d2[i]:
            if val > 1 and d2[i][0][1] == val:
                answer.append(key)
    
    answer.sort()
    
    return answer

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
