# 과일 장수

# my thoughts :
# 1. By using Queue, We can solve it..!!

from collections import deque

def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    score = deque(score)
    
    cnt = 0 # <<-- "현재 처리하고 있는 박스에 담겨져 있는 사과의 갯수"
    val = 0 # <<-- "현재 처리하고 있는 박스에 담겨져 있는 사과 중에서 점수가 가장 낮은 사과의 점수"
    for s in score:
        cnt += 1
        val = s
        
        if cnt == m:
            answer += val * cnt
            cnt = 0
        else:
            pass
    
    return answer
