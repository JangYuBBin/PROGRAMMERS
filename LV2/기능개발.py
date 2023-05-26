# 기능개발

# my thoughts :
# 1. By using Queue, We can solve it..!!

from collections import deque

def solution(progresses, speeds):
    answer = []
    for i in range(0, len(progresses), 1):
        q, r = divmod((100 - progresses[i]), speeds[i])
        
        if r == 0:
            progresses[i] = q
        else:
            progresses[i] = q + 1 # <<-- "즉, 해당 기능이 개발되는데 몇 일이 걸리는지 나타내주는 것입니다..!!"
    
    # print(progresses)
    # 출력결과 Ex : [7, 3, 9]
    
    progresses = deque(progresses)
    
    while progresses:
        cnt = 1
        cur_val = progresses.popleft()
        
        while progresses and progresses[0] <= cur_val:
            progresses.popleft()
            cnt += 1
        
        answer.append(cnt)
    return answer
