# 덧칠하기

from collections import deque

def solution(n, m, section):
    answer = 0
    
    section = deque(section)
    
    while section:
        answer += 1
        
        start = section[0]
        end = start + m - 1
        
        if end > n:
            start, end = start - (end - n), n # <<-- "경계를 벗어날 시 맞춰줍시다..!!"
        
        while section and start <= section[0] <= end:
            section.popleft()

    return answer
