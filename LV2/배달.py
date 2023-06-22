# 배달

# my thoughts :
# 1. By using Dijkstra Algorithm, We can solve it..!!
# 2. 즉, 1번 마을에서 다익스트라 알고리즘을 사용해서 각 마을까지의 최단 시간을 구한 후 배달 가능 여부를 결정합시다..!!

from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    h = []
    
    costs = [float("inf")] * (N + 1)
    
    heapq.heappush(h, (0, 1))
    # 참고 > (시간, 정점)
    costs[1] = 0
    
    while h:
        cur_cost, cur_v = heapq.heappop(h)
        
        if costs[cur_v] < cur_cost:
            continue
        
        for new_v, diff in graph[cur_v]:
            if costs[new_v] > cur_cost + diff:
                costs[new_v] = cur_cost + diff
                heapq.heappush(h, (cur_cost + diff, new_v))
    
    for v in range(1, N + 1, 1):
        if costs[v] <= K:
            answer += 1

    return answer
