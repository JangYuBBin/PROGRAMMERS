# 푸드 파이터 대회

def solution(food):
    answer = "0"
    
    for i in range(len(food) - 1, 0, -1):
        cnt = food[i] // 2
        
        answer = str(i) * cnt + answer + str(i) * cnt
        
    return answer

print(solution([1, 3, 4, 6]))
