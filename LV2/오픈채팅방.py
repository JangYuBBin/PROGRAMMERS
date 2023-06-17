# 오픈채팅방

# my thoughts :
# 1. 결국 어떤 유저 아이디가 마지막에 무슨 닉네임을 갖는지 체킹하면 됩니다..!!

from collections import defaultdict

def solution(record):
    answer = []
    
    d = defaultdict(str)
    
    for r in record:
        r = r.split()
        
        if r[0] == "Enter":
            d[r[1]] = r[2]
        elif r[0] == "Change":
            d[r[1]] = r[2]
    
    for r in record:
        r = r.split()
        
        if r[0] == "Enter":
            answer.append(d[r[1]] + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(d[r[1]] + "님이 나갔습니다.")
        else:
            pass
    
    return answer
