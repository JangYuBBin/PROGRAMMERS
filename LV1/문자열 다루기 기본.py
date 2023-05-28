# 문자열 다루기 기본

def solution(s):
    l = len(s)
    
    if l == 4 or l == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False
