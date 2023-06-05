# 네트워크

# my thoughts :
# 1. By using BFS Algorithm, We can solve it..!!

from collections import defaultdict
from collections import deque

def solution(n, computers):
    answer = 0
    
    graph = defaultdict(list)
    
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if i == j:
                continue
            else:
                if computers[i][j] == 1:
                    graph[i].append(j)
    
    visited = [False] * n
    
    for i in range(0, n, 1):
        if not visited[i]:
            answer += 1
            
            queue = deque()
            
            visited[i] = True
            queue.append(i)
            
            while queue:
                cur_v = queue.popleft()
                
                for new_v in graph[cur_v]:
                    if not visited[new_v]:
                        visited[new_v] = True
                        queue.append(new_v)
    
    return answer
