# 혼자서 하는 틱택토 

# my thoughts :
# 1. 일단 "O"의 갯수 - "X"의 갯수 = 1 or 0이 아니라면 규칙에 어긋나게 플레이한 경우입니다.
# 2. 그다음으로는 3 x 3 배열을 체킹했을 때 "O" 빙고의 갯수와 "X" 빙고의 갯수가 각각 (0, 0), (1, 0), (0, 1), (2, 0), (0, 2) 중 하나이어야 합니다.
# 3. (2, 0), (0, 2)인 경우는 한 번에 두 개의 빙고가 만들어지는 경우입니다.
# 4. (ex)
# ["OOO", "OXX", "OXX"]
# 5. 3, 4번을 생각해내는 것이 이 문제의 핵심 포인트입니다.
# 6. 틀린 문제이고 중요한 문제이므로 나중에 다시 풀어보아야 할 문제인 것 같습니다..!!

def solution(board): 
    # 일단 "O"의 갯수 - "X"의 갯수가 1 or 0인지 체킹합시다.
    check = 0
    
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if board[i][j] == "O":
                check += 1
            elif board[i][j] == "X":
                check -= 1
    
    if check == 1 or check == 0:
        pass
    else:
        return 0

    # 그다음으로는 "O"빙고의 갯수와 "X"빙고의 갯수를 확인한 다음 규칙에 맞게 플레이한 경우인지 판별하면 됩니다.
    # 일단 "O"빙고의 갯수부터 확인합시다.
    # 그런다음 "X"빙고의 갯수를 확인합시다..!!
    cnt_O = 0 # "O"빙고의 갯수
    cnt_X = 0 # "X"빙고의 갯수
    
    # 가로 "O"빙고
    if board[0][0] == board[0][1] == board[0][2] == "O":
        cnt_O += 1
    if board[1][0] == board[1][1] == board[1][2] == "O":
        cnt_O += 1
    if board[2][0] == board[2][1] == board[2][2] == "O":
        cnt_O += 1
    
    # 세로 "O"빙고
    if board[0][0] == board[1][0] == board[2][0] == "O":
        cnt_O += 1
    if board[0][1] == board[1][1] == board[2][1] == "O":
        cnt_O += 1
    if board[0][2] == board[1][2] == board[2][2] == "O":
        cnt_O += 1
        
    # 대각선 "O"빙고
    if board[0][0] == board[1][1] == board[2][2] == "O":
        cnt_O += 1
    if board[0][2] == board[1][1] == board[2][0] == "O":
        cnt_O += 1
    
    # 가로 "X"빙고
    if board[0][0] == board[0][1] == board[0][2] == "X":
        cnt_X += 1
    if board[1][0] == board[1][1] == board[1][2] == "X":
        cnt_X += 1
    if board[2][0] == board[2][1] == board[2][2] == "X":
        cnt_X += 1
    
    # 세로 "X"빙고
    if board[0][0] == board[1][0] == board[2][0] == "X":
        cnt_X += 1
    if board[0][1] == board[1][1] == board[2][1] == "X":
        cnt_X += 1
    if board[0][2] == board[1][2] == board[2][2] == "X":
        cnt_X += 1
        
    # 대각선 "X"빙고
    if board[0][0] == board[1][1] == board[2][2] == "X":
        cnt_X += 1
    if board[0][2] == board[1][1] == board[2][0] == "X":
        cnt_X += 1
        
    # 빙고 개수에 따라 결과 반환
    if cnt_O == 0 and cnt_X == 0:
        return 1
    elif cnt_O == 1 and cnt_X == 0 and check == 1:
        return 1
    elif cnt_O == 0 and cnt_X == 1 and check == 0:
        return 1
    elif cnt_O == 2 and cnt_X == 0 and check == 1:
        return 1
    elif cnt_O == 0 and cnt_X == 2 and check == 0:
        return 1
    else:
        return 0
