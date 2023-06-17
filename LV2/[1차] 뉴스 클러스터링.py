# [1차] 뉴스 클러스터링

from collections import defaultdict

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    # print(str1)
    # print(str2)
    # ....
    
    d1 = defaultdict(int) # str1용
    d2 = defaultdict(int) # str2용
    
    for i in range(0, len(str1) - 1, 1):
        temp = str1[i:i+2:1]
        if temp.isalpha():
            pass
        else:
            continue
        
        d1[temp] += 1
    
    for i in range(0, len(str2) - 1, 1):
        temp = str2[i:i+2:1]
        if temp.isalpha():
            pass
        else:
            continue
        
        d2[temp] += 1
    
    intersection = set(d1.keys()).intersection(set(d2.keys()))
    union = set(d1.keys()).union(set(d2.keys()))
    
    # print(intersection, union)
    # 출력결과 Ex : {'aa', 'a1'} {'aa', '1+', 'a2', '12', '+a', 'a1'}
    
    num1 = 0
    
    for c in list(intersection):
        num1 += min(d1[c], d2[c])
    
    num2 = 0
    
    for c in list(union):
        num2 += max(d1[c], d2[c])
    
    if num2 == 0:
        return 1 * 65536
    else:
        return int((num1 / num2) * 65536)
