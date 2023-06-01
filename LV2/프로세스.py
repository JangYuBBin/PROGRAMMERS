# 프로세스 

# my thoughts :
# 1. By using Queue, We can solve it..!!

from collections import deque

def solution(priorities, location):
    answer = 0
    
    priorities = [(priority, i) for i, priority in enumerate(priorities)]
    
    # print(priorities)
    # 출력결과 Ex : [(2, 0), (1, 1), (3, 2), (2, 3)]
    
    queue = deque(priorities)
    
    while queue:
        cur_priority, idx = queue.popleft()

        checkFlag = True

        for p, i in queue:
            if cur_priority < p:
                checkFlag = False
                break
        
        if checkFlag == True:
            if idx == location:
                answer += 1
                return answer
            else:
                answer += 1
        else:
            queue.append((cur_priority, idx))
    
print(solution([2, 1, 3, 2], 2))
