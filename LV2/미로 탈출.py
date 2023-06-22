# 미로 탈출

# my thoughts :
# 1. By using BFS Algorithm, We can solve it..!!
# 2. 미로를 탈출하는데 필요한 최소 시간 = 시작 지점에서 레버까지 가는데 걸리는 최소 시간 + 레버에서 출구까지 가는데 걸리는 최소 시간

from collections import deque

def solution(maps):
    global answer
    answer = 0

    global checkFlag
    checkFlag = True
    
    def fromStoL(start_v):
        global answer
        global checkFlag

        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        queue = deque()
        
        visited[start_v[0]][start_v[1]] = True
        queue.append((start_v, 0))
        
        while queue:
            cur_v, cur_cnt = queue.popleft()
            
            if maps[cur_v[0]][cur_v[1]] == "L":
                answer += cur_cnt
                return
            
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
                
                if 0 <= new_v[0] < len(maps) and 0 <= new_v[1] < len(maps[0]) and not visited[new_v[0]][new_v[1]] and maps[new_v[0]][new_v[1]] != "X":
                    visited[new_v[0]][new_v[1]] = True
                    queue.append((new_v, cur_cnt + 1))
        
        checkFlag = False
        return

    def fromLtoE(start_v):
        global answer
        global checkFlag 

        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        queue = deque()
        
        visited[start_v[0]][start_v[1]] = True
        queue.append((start_v, 0))
        
        while queue:
            cur_v, cur_cnt = queue.popleft()
            
            if maps[cur_v[0]][cur_v[1]] == "E":
                answer += cur_cnt
                return
            
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
                
                if 0 <= new_v[0] < len(maps) and 0 <= new_v[1] < len(maps[0]) and not visited[new_v[0]][new_v[1]] and maps[new_v[0]][new_v[1]] != "X":
                    visited[new_v[0]][new_v[1]] = True
                    queue.append((new_v, cur_cnt + 1))
        
        checkFlag = False
        return
    
    S = [0, 0]
    L = [0, 0]

    for i in range(0, len(maps), 1):
        for j in range(0, len(maps[0]), 1):
            if maps[i][j] == "S":
                S = [i, j]
            elif maps[i][j] == "L":
                L = [i, j]
    
    fromStoL(S)
    fromLtoE(L)

    if checkFlag:
        return answer
    else:
        return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
