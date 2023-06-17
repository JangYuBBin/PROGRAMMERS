# 신고 결과 받기

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    d = dict()
    for id in id_list:
        d[id] = set()
    # 참고 > 딕셔너리 자료형 d의 키는 신고를 받은 사람이며 값은 신고를 한 사람들을 모은 리스트 자료형입니다.
    
    for r in report:
        r = r.split()
        
        d[r[1]].add(r[0])
    
    # print(d)
    # 출력결과 Ex : 	{'muzi': {'apeach'}, 'frodo': {'muzi', 'apeach'}, 'apeach': set(), 'neo': {'muzi', 'frodo'}}
    
    for key in d.keys():
        d[key] = list(d[key])
    
    # print(d)
    # 출력결과 Ex : {'muzi': ['apeach'], 'frodo': ['apeach', 'muzi'], 'apeach': [], 'neo': ['frodo', 'muzi']}
    
    cnt = dict()
    for id in id_list:
        cnt[id] = 0
    
    for key in d.keys():
        if len(d[key]) >= k:
            for name in d[key]:
                cnt[name] += 1
    
    for id in id_list:
        answer.append(cnt[id])
    
    return answer
