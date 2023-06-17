# [3차] 압축

# my thoughts :
# 1. 문제의 조건에 맞게 구현..!!
# 2. 맞으면 ok..!!

def solution(msg):
    answer = []
    
    d = dict()
    for i, c in enumerate(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]):
        d[c] = i + 1
    
    start = 0
    end = 0
    
    while True:
        if end <= len(msg) - 1 and msg[start:end + 1:1] in d:
            end += 1
        elif end <= len(msg) - 1 and msg[start:end + 1:1] not in d:
            answer.append(d[msg[start:end:1]])
            d[msg[start:end + 1:1]] = len(d) + 1
            start = end
        else:
            answer.append(d[msg[start:end:1]])
            break
        
    return answer

print(solution("KAKAO"))
