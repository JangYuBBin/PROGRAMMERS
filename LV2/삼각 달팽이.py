# 삼각 달팽이

# my thoughts :
# 1. 규칙에 맞게 배열을 채워봅시다..!!

def solution(n):
    temp = [[0] * n for _ in range(n)]
    answer = list()
    
    go = n
    val = 0
    x = -1
    y = 0
    
    while True:
        if go == 0:
            break
        else:
            pass
        
        for _ in range(go):
            x += 1
            val += 1
            
            temp[x][y] = val
        
        go -= 1
        
        if go == 0:
            break
        else:
            pass
        
        for _ in range(go):
            y += 1
            val += 1
            
            temp[x][y] = val
        
        go -= 1
        
        if go == 0:
            break
        else:
            pass
        
        for _ in range(go):
            x -= 1
            y -= 1
            val += 1
            
            temp[x][y] = val
        
        go -= 1
    
    # print(temp)
    # 출력결과 Ex : [[1, 0, 0, 0], [2, 9, 0, 0], [3, 10, 8, 0], [4, 5, 6, 7]]
    
    for i in range(0, n, 1):
        for j in range(0, i + 1, 1):
            answer.append(temp[i][j])
    
    return answer
