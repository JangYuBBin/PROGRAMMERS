# 최소직사각형

def solution(sizes):
    answer = 0
    
    for i in range(0, len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            pass
        else:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    garo = 0
    sero = 0
    
    for i in range(0, len(sizes)):
        if sizes[i][0] > garo:
            garo = sizes[i][0]
        if sizes[i][1] > sero:
            sero = sizes[i][1]
    
    answer = garo * sero
    
    return answer
