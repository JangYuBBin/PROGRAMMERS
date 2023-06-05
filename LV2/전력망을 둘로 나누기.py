# 전력망을 둘로 나누기

# my thoughts :
# 1. 양방향 그래프 구축
# 2. wires 리스트를 순회하면서 간선 하나를 제거 후 두 전력망이 가지고 있는 송전탑 개수의 차이를 구함.
# 3. 구했다면 다시 원래상태로 되돌리기 위하여 간선 하나를 다시 추가..!!

from collections import defaultdict
from collections import deque

def solution(n, wires):
    answer = []
    
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        cnt = 0 
        
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = [False] * (n + 1)
        visited[1] = True
        
        queue = deque()
        queue.append(1)
        
        cnt += 1
        
        while queue:
            cur_v = queue.popleft()
            
            for new_v in graph[cur_v]:
                if not visited[new_v]:
                    visited[new_v] = True
                    queue.append(new_v)
                    cnt += 1
        
        diff = abs((n - cnt) - cnt)
        
        answer.append(diff)

        graph[v1].append(v2)
        graph[v2].append(v1)
    
    answer.sort()
    
    return answer[0]

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
