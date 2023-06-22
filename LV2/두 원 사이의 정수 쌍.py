# 두 원 사이의 정수 쌍

# my thoughts :
# 1. 1사분면에서의 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수 * 4 ==>> answer

from math import sqrt

def solution(r1, r2):
    answer = 0
    
    # 큰 원에 존재하는 정수 좌표들(경계선 포함)
    for x in range(0, r2 + 1, 1):
        y = sqrt(r2**2 - x**2)
        y = int(y)
        
        answer += y + 1
    
    # 작은 원에 존재하는 정수 좌표들(경계선 미포함)
    for x in range(0, r1 + 1, 1):
        y = sqrt(r1**2 - x**2)
        
        if y % 1 == 0:
            answer -= int(y)
        else:
            answer -= int(y + 1)
    
    answer *= 4
    
    # 겹치는 부분 제거..!!
    answer -= 4 * (r2 - r1 + 1)
    
    return answer

print(solution(2, 3))
