# 게임 맵 최단거리

# my thoughts :
# 1. By using BFS Algorithm, We can solve it..!!

from collections import deque

def solution(maps):
    answer = 0
    distance = [[float("inf")] * len(maps[0]) for _ in range(len(maps))]
    distance[0][0] = 1
    
    queue = deque()
    
    queue.append((0, 0))
    
    while queue:
        cur_v = queue.popleft()
        
        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
            
            if 0 <= new_v[0] < len(maps) and 0 <= new_v[1] < len(maps[0]) and maps[new_v[0]][new_v[1]] == 1:
                if distance[new_v[0]][new_v[1]] > distance[cur_v[0]][cur_v[1]] + 1:
                    distance[new_v[0]][new_v[1]] = distance[cur_v[0]][cur_v[1]] + 1
                    queue.append(new_v)
    
    answer = distance[len(maps) - 1][len(maps[0]) - 1]
    
    if answer == float("inf"):
        return -1
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
