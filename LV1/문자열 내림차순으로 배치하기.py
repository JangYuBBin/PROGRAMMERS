# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    
    s = list(s)
    s.sort(reverse = True)
    
    answer = "".join(s)
    
    return answer
