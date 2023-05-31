# 완주하지 못한 선수

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!

def solution(participant, completion):
    answer = ''
    
    d = dict()
    
    for p in participant:
        if p not in d:
            d[p] = 1
        else:
            d[p] += 1
    
    for c in completion:
        d[c] -= 1
    
    for k in d.keys():
        if d[k] != 0:
            answer = k
            break

    return answer
