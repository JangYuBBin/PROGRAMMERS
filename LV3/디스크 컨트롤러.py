# 디스크 컨트롤러

# my thoughts :
# 1. By using Heap, We can solve it..!!
# 2. 만약 현재 시점에서 이미 들어온 작업 요청이 2개 이상이라면, 작업의 소요시간이 가장 적은 작업을 하나 처리한다.
# 3. 만약 현재 시점에서 작업 요청이 1개도 들어오지 않았다면, 현재 시점을 +1 처리 해준다..!!

import heapq

def solution(jobs):
    answer = 0
    l = len(jobs)
    
    h = []
    
    for job in jobs:
        heapq.heappush(h, (job[0], job[1]))
    
    cur_time = 0
    temp = []
    
    while h:
        while h and h[0][0] <= cur_time:
            start_time, diff = heapq.heappop(h)
            
            heapq.heappush(temp, (diff, start_time))
        
        if temp:
            diff, start_time = heapq.heappop(temp)
            
            answer += (cur_time - start_time) + diff
            cur_time += diff
            
            while temp:
                diff, start_time = heapq.heappop(temp)
                
                heapq.heappush(h, (start_time, diff))
        else:
            cur_time += 1

    answer = int(answer / l)
        
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))
