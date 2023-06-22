# 부대복귀

# my thoughts :
# 1. 문제에서 주어진 간선은 양방향 간선입니다.
# 2. 따라서 우리는 각 source에서 destination으로 가는 것이 아닌 반대로 생각하여 destination에서 각 source로 가는 식으로 다익스트라 알고리즘 혹은 BFS 탐색을 진행해야 합니다.
# 3. 2번이 이 문제의 시간초과 판정을 피하는 핵심 로직입니다..!!
# 4. 또한 어차피 각 노드 사이의 간선의 길이가 1로 고정되어 있기 때문에 우리는 힙 자료구조를 활용할 필요가 없습니다. -->> 따라서 큐 자료구조를 활용하여 시간 복잡도를 단축할 수 있습니다..!! + 큐 자료구조를 활용한 풀이는 내일 다시 풀어보도록 합시다..!!

from collections import defaultdict
import heapq

def solution(n, roads, sources, destination):
    answer = []
    
    graph = defaultdict(list)
    
    for v1, v2 in roads:
        graph[v1].append((v2, 1))
        graph[v2].append((v1, 1))
    
    # print(graph)
    # 출력결과 Ex : defaultdict(<class 'list'>, {1: [(2, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1)]})
    
    costs = [float("inf")] * (n + 1)
    
    def dijkstra(start_v):
        h = []
        
        costs[start_v] = 0
        heapq.heappush(h, (0, start_v))
        
        while h:
            cur_cost, cur_v = heapq.heappop(h)
            
            if costs[cur_v] < cur_cost:
                continue
                
            for new_v, diff in graph[cur_v]:
                if costs[new_v] > cur_cost + diff:
                    costs[new_v] = cur_cost + diff
                    heapq.heappush(h, (cur_cost + diff, new_v))
    
    dijkstra(destination)
    
    for source in sources:
        if costs[source] == float("inf"):
            answer.append(-1)
        else:
            answer.append(costs[source])
    
    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
