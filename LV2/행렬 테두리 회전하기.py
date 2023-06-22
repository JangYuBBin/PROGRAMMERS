# 행렬 테두리 회전하기

# my thoughts :
# 1. 구현 문제인 것 같습니다..!!

def solution(rows, columns, queries):
    answer = []
    
    board = list()
    
    val = 0
    
    for i in range(0, rows, 1):
        cur_row = list()
        
        for j in range(0, columns, 1):
            val += 1
            cur_row.append(val)
        
        board.append(cur_row)
    
    # print(board)
    # 출력결과 Ex : 	[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
    
    def rotate(query):
        start_x = query[0] - 1
        start_y = query[1] - 1
        end_x = query[2] - 1
        end_y = query[3] - 1
        
        # before = board[:]
        # after = board[:]
        
        after = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(0, len(board), 1):
            for j in range(0, len(board[0]), 1):
                after[i][j] = board[i][j]
        
        points = list() # <<-- "테두리에 있는 좌표들을 담을 1차원 리스트의 선언입니다..!!"
        
        # 좌 -->> 우
        for i in range(start_x, start_x + 1, 1):
            for j in range(start_y, end_y + 1, 1):
                points.append((i, j))
        
        # 상 -->> 하
        for i in range(start_x + 1, end_x + 1, 1):
            for j in range(end_y, end_y + 1, 1):
                points.append((i, j))
        
        # 우 -->> 좌
        for i in range(end_x, end_x + 1, 1):
            for j in range(end_y - 1, start_y - 1, -1):
                points.append((i, j))
        
        # 하 -->> 상
        for i in range(end_x - 1, start_x, -1):
            for j in range(start_y, start_y + 1, 1):
                points.append((i, j))
        
        min_val = float("inf")
        
        for i in range(0, len(points), 1):
            after[points[i][0]][points[i][1]] = board[points[i - 1][0]][points[i - 1][1]]

            if min_val > board[points[i - 1][0]][points[i - 1][1]]:
                min_val = board[points[i - 1][0]][points[i - 1][1]]
        
        for i, j in points:
            board[i][j] = after[i][j]
        
        return min_val
        
    for query in queries:
        answer.append(rotate(query))
        
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
