# 순위 검색

# my thoughts :
# 1. 문제의 조건에 맞게 구현
# 2. 시간초과를 피하기 위해서 bisect 라이브러리를 활용합시다..!!

from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    d = defaultdict(list)
    
    for i in info:
        i = i.split()
        
        for c1 in [i[0], "-"]:
            for c2 in [i[1], "-"]:
                for c3 in [i[2], "-"]:
                    for c4 in [i[3], "-"]:
                        temp = c1 + c2 + c3 + c4
                        
                        d[temp].append(int(i[4]))
    
    # print(d)
    # 출력결과 Ex : 	defaultdict(<class 'list'>, {'javabackendjuniorpizza': [150], 'javabackendjunior-': [150, 80], 'javabackend-pizza': [150], '.... }
    
    for k in d.keys():
        d[k].sort(reverse = False)

    # print(d)
    # 출력결과 Ex : .... ----': [50, 80, 150, 150, 210, 260] .... 
        
    for q in query:
        temp = q.split()
        
        check = ""
        score = 0
        
        for t in temp:
            if t == "and":
                continue
            elif t.isdigit():
                score = int(t)
            else:
                check += t
        
        # print(check)
        # print(score)
        # ----
        # 150

        answer.append(len(d[check]) - bisect_left(d[check], score))
            
    
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
