# 혼자 놀기의 달인

# my thoughts :
# 1. By using BFS, We can solve it..!!

from collections import deque
from collections import defaultdict

def solution(cards):
    answer = list()
    
    graph = defaultdict(list)
    
    for i in range(0, len(cards), 1):
        graph[i + 1].append(cards[i])
        
    visited = [False] * (len(cards) + 1)
    
    def bfs(start_v):
        answer = 0 # <<-- "방문한 정점의 수를 나타낼 변수의 선언입니다..!!"
        
        queue = deque()
        
        visited[start_v] = True
        queue.append(start_v)
        answer += 1
        
        while queue:
            cur_v = queue.popleft()
            
            for new_v in graph[cur_v]:
                if not visited[new_v]:
                    visited[new_v] = True
                    queue.append(new_v)
                    answer += 1
        
        return answer
    
    for v in range(1, len(cards) + 1, 1):
        if not visited[v]:
            answer.append(bfs(v))
    
    answer.sort(reverse = True)
    
    if len(answer) == 1:
        return 0
    else:
        return answer[0] * answer[1]
