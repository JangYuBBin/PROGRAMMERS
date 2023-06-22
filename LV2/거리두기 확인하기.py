# 거리두기 확인하기

from collections import deque

def solution(places):
    answer = []
    
    for place in places:
        checkFlag = True
        
        start_vs = list()
        
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                if place[i][j] == "P":
                    start_vs.append((i, j))
        
        # print(start_vs)
        # 출력결과 Ex : [(0, 0), (0, 4), (2, 1), (2, 3), (4, 0), (4, 4)]
        
        for start_v in start_vs:
            visited = [[False] * 5 for _ in range(5)]
            queue = deque()
            
            visited[start_v[0]][start_v[1]] = True
            queue.append((0, start_v))
            
            while queue:
                cur_cnt, cur_v = queue.popleft()
                
                if cur_cnt == 2: # <<-- "맨허튼 거리가 2이하인 경우만 고려하면 되기 때문입니다..!!"
                    continue
                
                for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
                    
                    if 0 <= new_v[0] < 5 and 0 <= new_v[1] < 5 and not visited[new_v[0]][new_v[1]]:
                        if place[new_v[0]][new_v[1]] == "P":
                            checkFlag = False
                            break
                        elif place[new_v[0]][new_v[1]] == "O":
                            visited[new_v[0]][new_v[1]] = True
                            queue.append((cur_cnt + 1, new_v))
                
                if checkFlag == False:
                    break
                else:
                    pass
            
            if checkFlag == False:
                break
            else:
                pass
        
        if checkFlag == True:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
