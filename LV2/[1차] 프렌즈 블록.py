# [1차] 프렌즈 블록

# my thoughts :
# 1. 블록이 지워진 후 2차원 배열의 재조정이 필요하다.
# 2. 2차원 배열의 재조정을 편리하게 하기 위해서 그 전에 2차원 배열의 행과 열을 바꿔주는 작업을 해주어야 한다.
# 3. ....

def solution(m, n, board):
    answer = 0
    
    board = list(map(list, zip(*board)))
    # print(board)
    # 출력결과 Ex : [['C', 'A', 'A', 'C'], ['C', 'A', 'A', 'C'], ['B', 'A', 'A', 'B'], ['D', 'D', 'B', 'B'], ['E', 'E', 'F', 'F']]
    
    while True:
        locations = set() # <<-- "이번 턴에 폭발되는 좌표들을 담을 1차원 리스트의 선언입니다..!!"
        
        for i in range(0, n - 1):
            for j in range(0, m - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != "X":
                    locations.add((i, j))
                    locations.add((i, j + 1))
                    locations.add((i + 1, j))
                    locations.add((i + 1, j + 1))
        
        answer += len(locations)
        locations = list(locations)
        
        if not locations:
            break
        else:
            for i, j in locations:
                board[i][j] = "X"
        
        for i in range(0, n):
            temp2 = [val for val in board[i] if val != "X"]
            temp1 = [val for val in board[i] if val == "X"]
            
            board[i] = temp1 + temp2
    
    return answer
