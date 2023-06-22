# 리코쳇 로봇

# my thoughts :
# 1. By using BFS, We can solve it..!!
# 2. 기존 board 배열을 변환해서 문제에 접근해보자.
# 3. 즉, 테두리 부분에 추가로 D를 덧붙여서 ..!!
# 4. 이렇게 변환한다면 문제에 조금 더 쉽게 접근할 수 있기 때문입니다..!!

from collections import deque

def solution(board):
    answer = 0
    
    new_board = list()
    new_board.append("D" * (len(board[0]) + 2))
    
    for i in range(0, len(board), 1):
        new_board.append("D" + board[i] + "D")
    
    new_board.append("D" * (len(board[0]) + 2))
    
    # print(new_board)
    # 출력결과 Ex : ['DDDDDDDDD', 'D...D..RD', 'D.D.G...D', 'D....D.DD', 'DD....D.D', 'D..D....D', 'DDDDDDDDD']
    
    board = new_board
    
    # print(board)
    # 출력결과 Ex : ['DDDDDDDDD', 'D...D..RD', 'D.D.G...D', 'D....D.DD', 'DD....D.D', 'D..D....D', 'DDDDDDDDD']
    
    def bfs(start_v, end_v):
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        queue = deque()
        
        visited[start_v[0]][start_v[1]] = True
        queue.append((0, start_v))
        
        while queue:
            cur_cnt, cur_v = queue.popleft()
            
            if cur_v == end_v:
                return cur_cnt
            else:
                pass

            # 상
            for i in range(cur_v[0], -1, -1):
                if board[i][cur_v[1]] == ".":
                    pass
                elif board[i][cur_v[1]] == "D":
                    break
            
            new_v = (i + 1, cur_v[1])

            if not visited[new_v[0]][new_v[1]]:
                visited[new_v[0]][new_v[1]] = True
                queue.append((cur_cnt + 1, new_v))
            
            # 하
            for i in range(cur_v[0], len(board), 1):
                if board[i][cur_v[1]] == ".":
                    pass
                elif board[i][cur_v[1]] == "D":
                    break
            
            new_v = (i - 1, cur_v[1])

            if not visited[new_v[0]][new_v[1]]:
                visited[new_v[0]][new_v[1]] = True
                queue.append((cur_cnt + 1, new_v))
            
            # 좌
            for j in range(cur_v[1], -1, -1):
                if board[cur_v[0]][j] == ".":
                    pass
                elif board[cur_v[0]][j] == "D":
                    break
            
            new_v = (cur_v[0], j + 1)

            if not visited[new_v[0]][new_v[1]]:
                visited[new_v[0]][new_v[1]] = True
                queue.append((cur_cnt + 1, new_v))
            
            # 우
            for j in range(cur_v[1], len(board[0]), 1):
                if board[cur_v[0]][j] == ".":
                    pass
                elif board[cur_v[0]][j] == "D":
                    break
            
            new_v = (cur_v[0], j - 1)

            if not visited[new_v[0]][new_v[1]]:
                visited[new_v[0]][new_v[1]] = True
                queue.append((cur_cnt + 1, new_v))
        
        return -1
    
    start_v = (0, 0)
    end_v = (0, 0)

    for i in range(0, len(board), 1):
        for j in range(0, len(board[0]), 1):
            if board[i][j] == "R":
                start_v = (i, j)
            elif board[i][j] == "G":
                end_v = (i, j)
    
    return bfs(start_v, end_v)

print(solution([".D.R", "....", ".G..", "...D"]))
