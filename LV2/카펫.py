# 카펫

# my thoughts :
# 1. garo * sero = brown + yellow
# 2. brown = 2 * garo + 2 * (sero - 1)
# 3. 카펫의 가로 길이는 세로 길이보다 같거나 큽니다.

def solution(brown, yellow):
    answer = [0, 0]
    
    for garo in range(brown + yellow, 0, -1):
        sero = (brown + yellow) / garo
        
        if sero % 1 == 0 and brown == 2 * garo + 2 * (sero - 2):
            answer[0] = garo
            answer[1] = int(sero)
            break
                    
    return answer

print(solution(10, 2))
