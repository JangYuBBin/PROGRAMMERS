# 후보키

# my thoughts :
# 1. 조합 라이브러리를 활용하여 문제에 접근해봅시다..!!
# 2. ....

from itertools import combinations

def solution(relation):
    answer = list()
    
    cases = list()
    
    for i in range(1, len(relation), 1):
        temp = list(combinations(list(range(0, len(relation[0]), 1)), i))
        
        cases.extend(temp)
    
    # print(cases)
    # 출력결과 Ex : [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
    
    for case in cases:
        check = set()
        
        for r in relation:
            temp = list()
            
            for i in case:
                temp.append(r[i])
            
            temp = tuple(temp)
            check.add(temp)
        
        if len(check) == len(relation):
            if not answer:
                answer.append(case)
            else:
                checkFlag = True
                
                for a in answer:
                    checkCnt = 0
                    
                    for i in range(0, len(a), 1):
                        if a[i] in case:
                            checkCnt += 1
                        else:
                            pass
                    
                    if checkCnt == len(a):
                        checkFlag = False
                        break
                    else:
                        pass
                
                if checkFlag == True:
                    answer.append(case)
                else:
                    pass
        else:
            pass
    
    return len(answer)
