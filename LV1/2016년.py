# 2016년

def solution(a, b):
    answer = ''
    
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    diff = 0
    
    for i in range(1, a):
        if i == 2:
            diff += 29
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            diff += 31
        else:
            diff += 30
    diff += (b - 1)
    
    answer = days[diff % 7]
    
    return answer
