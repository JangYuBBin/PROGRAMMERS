# 가운데 글자 가져오기

def solution(s):
    l = len(s)
    
    if l % 2 == 0:
        return s[l // 2 - 1] + s[l // 2]
    else:
        return s[l // 2]
        
