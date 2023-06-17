# 무인도 여행

# my thoughts :
# 1. By using BFS, We can solve it..!!

from collections import deque

def solution(maps):
    answer = []

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    def bfs(start_v):
        food = 0
        queue = deque()
        
        visited[start_v[0]][start_v[1]] = True
        queue.append(start_v)
        food += int(maps[start_v[0]][start_v[1]])
        
        while queue:
            cur_v = queue.popleft()
            
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
                
                if 0 <= new_v[0] < len(maps) and 0 <= new_v[1] < len(maps[0]) and maps[new_v[0]][new_v[1]] != "X" and not visited[new_v[0]][new_v[1]]:
                    visited[new_v[0]][new_v[1]] = True
                    queue.append(new_v)
                    food += int(maps[new_v[0]][new_v[1]])
        
        return food

    for i in range(0, len(maps)):
        for j in range(0, len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                answer.append(bfs((i, j)))
    
    if not answer:
        return [-1]
    else:
        answer.sort(reverse = False)
        
        return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))
