# 크레인 인형뽑기 게임

# my thoughts :
# 1. 조작을 편하게 하기 위해서 2차원 배열 board의 행과 열을 바꾼 후 접근해 봅시다.
# 2. 해당 행이 [0] * len(board)인 상태라면 그 행에서는 꺼낼 인형이 없는 상태라는 것입니다.
# 3. ....

def solution(board, moves):
    answer = 0
    
    board = list(map(list, zip(*board)))
    # print(board)
    # 출력결과 Ex : [[0, 0, 0, 4, 3], [0, 0, 2, 2, 5], [0, 1, 5, 4, 1], [0, 0, 0, 4, 3], [0, 3, 1, 2, 1]]
    
    stack = [] # <<-- "바구니를 의미합니다..!!"
    
    for move in moves:
        move -= 1
        
        if board[move] == [0] * len(board): # <<-- "해당 행에서 꺼낼 인형이 없는 상태입니다..!!"
            continue
        else:
            pass
        
        for i in range(0, len(board[move])):
            if board[move][i] == 0:
                pass
            else:
                stack.append(board[move][i])
                board[move][i] = 0
                break
        
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
    
    return answer
