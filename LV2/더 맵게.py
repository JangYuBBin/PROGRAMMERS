# 더 맵게

# my thoughts :
# 1. By using Minimum Heap Algorithm, We can solve it..!!

import heapq

def solution(scoville, K):
    answer = 0
    
    h = [] # <<-- "최소 힙 운용..!!"
    for scv in scoville:
        heapq.heappush(h, scv)
    
    while len(h) >= 2 and h[0] < K:
        s1 = heapq.heappop(h)
        s2 = heapq.heappop(h)
        
        new_s = s1 + s2 * 2
        
        heapq.heappush(h, new_s)
        
        answer += 1
    
    if h[0] < K:
        return -1
    else:
        return answer
