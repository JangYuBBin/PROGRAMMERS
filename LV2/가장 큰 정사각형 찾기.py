# 가장 큰 정사각형 찾기

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 현재 확인하고 있는 좌표 (x, y)의 값이 1일 때, (x - 1, y), (x, y - 1), (x - 1, y - 1) 좌표의 값의 min()값에 +1한 값이 현재 좌표에서 만들 수 있는 최대 정사각형의 한 변의 길이입니다..!!

def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
    
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if answer < board[i][j]:
                answer = board[i][j]
    
    answer = answer**2

    return answer
