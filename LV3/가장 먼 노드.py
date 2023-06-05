# 가장 먼 노드

# my thoughts :
# 1. By using Dijkstra Algorithm, We can solve it..!!

from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    costs = [float("inf")] * (n + 1)
    costs[1] = 0
    
    queue = deque()
    
    queue.append((1, 0))
    
    while queue:
        cur_v, cur_cnt = queue.popleft()
        
        if costs[cur_v] < cur_cnt:
            continue
        
        for new_v in graph[cur_v]:
            if costs[new_v] > cur_cnt + 1:
                costs[new_v] = cur_cnt + 1
                queue.append((new_v, cur_cnt + 1))
    
    check = list()
    
    for v in range(2, n + 1, 1):
        check.append((v, costs[v]))
    
    check.sort(key = lambda x : x[1], reverse = True)
    
    for v, distance in check:
        if check[0][1] != distance:
            break
        else:
            answer += 1
        
    return answer
