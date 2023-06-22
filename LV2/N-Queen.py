# N-Queen

# my thoughts :
# 1. By using BackTracking, We can solve it..!!
# 2. 마지막 테스트 케이스의 시간초과 판정을 피하기 위해서 약간의 센스가 필요했던 문제였습니다..!!

def solution(n):
    global answer
    answer = 0
    
    global board
    board = []
    
    def dfs(row): # <<-- "현재 확인하고 있는 row 행에 대해서 검사..!!"
        global answer
        global board
        
        if row == n:
            answer += 1
        elif row < n:
            for col in range(0, n, 1):
                checkFlag = True
                
                for i in range(0, row, 1):
                    if board[i] == col or (row - i) == abs(col - board[i]):
                        checkFlag = False
                        break
                    else:
                        pass
                
                if checkFlag == True:
                    board.append(col)
                    
                    dfs(row + 1)
                    
                    board.pop()
                else:
                    pass
    
    dfs(0)
        
    return answer
