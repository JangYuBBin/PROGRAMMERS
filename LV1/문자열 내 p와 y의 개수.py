# 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    
    p_cnt = 0
    y_cnt = 0
    
    for c in s:
        if c == "p":
            p_cnt += 1
        elif c == "y":
            y_cnt += 1
    
    if p_cnt == y_cnt:
        return True
    else:
        return False
