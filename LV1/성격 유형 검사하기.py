# 성격 유형 검사하기

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!

from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    d = defaultdict(int)
    
    for s, choice in zip(survey, choices):
        if 1 <= choice <= 3:
            d[s[0]] += 4 - choice
        elif 5 <= choice <= 7:
            d[s[1]] += choice - 4
    
    for zipyo in ["RT", "CF", "JM", "AN"]:
        if d[zipyo[0]] > d[zipyo[1]]:
            answer += zipyo[0]
        elif d[zipyo[0]] < d[zipyo[1]]:
            answer += zipyo[1]
        else:
            answer += zipyo[0]
    
    return answer
