# 야근 지수

# my thoughts :
# 1. By using Max Heap, We can solve it..!!

import heapq

def solution(n, works):
    answer = 0
    
    h = []
    
    for work in works:
        heapq.heappush(h, -work)
    
    for _ in range(n):
        work = heapq.heappop(h)
        work += 1

        if work == 0:
            pass
        elif work < 0:
            heapq.heappush(h, work)
        
        if not h:
            break
    
    h = [val**2 for val in h]

    return sum(h)

print(solution(4, [4, 3, 3]))
