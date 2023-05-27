# 하샤드 수

def solution(x):
    check = sum(list(map(int, list(str(x)))))
    
    if x % check == 0:
        return True
    else:
        return False
