# 바탕화면 정리

# my thoughts :
# 1. By using Brute Force, We can solve it..!!

def solution(wallpaper):
    answer = [0, 0, 0, 0]
    
    min_x = float("inf")
    min_y = float("inf")
    max_x = 0
    max_y = 0
    
    for i in range(0, len(wallpaper)):
        for j in range(0, len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                if min_x > i:
                    min_x = i
            
                if min_y > j:
                    min_y = j
                
                if max_x < i:
                    max_x = i
            
                if max_y < j:
                    max_y = j
    
    max_x += 1
    max_y += 1
    
    answer[0] = min_x
    answer[1] = min_y
    answer[2] = max_x
    answer[3] = max_y
    
    return answer
