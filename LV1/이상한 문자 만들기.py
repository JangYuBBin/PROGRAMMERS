# 이상한 문자 만들기

def solution(s):
    answer = ""
    
    idx = 0
    for i in range(0, len(s)):
        if i == 0:
            answer += s[i].upper()
            idx += 1
        elif s[i] == " ":
            answer += s[i]
        elif s[i - 1] == " " and s[i] != " ":
            idx = 0
            answer += s[i].upper()
            idx += 1
        else:
            if idx % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            idx += 1
        
    return answer
