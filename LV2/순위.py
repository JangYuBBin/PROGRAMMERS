# 순위

# my thoughts :
# 1. By using Graph, We can solve it..!!

from collections import defaultdict
from collections import deque

def solution(n, results):
    answer = 0
    
    score = [[0, 0] for _ in range(n + 1)]
    
    graph = defaultdict(list)
    for v1, v2 in results:
        graph[v1].append(v2)
    
    for i in range(1, n + 1, 1):
        start_v = i
        
        wins = set()
        
        queue = deque()
        
        queue.append(start_v)
        
        while queue:
            cur_v = queue.popleft()
            
            for new_v in graph[cur_v]:
                if new_v not in wins:
                    wins.add(new_v)
                    queue.append(new_v)
        
        for v in list(wins):
            score[start_v][0] += 1
            score[v][1] += 1
    
    for v in range(1, n + 1, 1):
        if sum(score[v]) == n - 1:
            answer += 1
        else:
            pass
    
    return answer
