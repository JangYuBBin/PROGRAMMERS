# 요격 시스템

# my thoughts :
# 1. 입출력 예 설명 그림에 문제의 힌트가 있는 문제였습니다..!!
# 2. ....

def solution(targets):
    answer = 1
    
    targets.sort(key = lambda x : x[1], reverse = False)
    
    # print(targets)
    # 출력결과 Ex : [[1, 4], [4, 5], [3, 7], [4, 8], [5, 12], [11, 13], [10, 14]]
    
    criterion = targets[0][1]
    
    for i in range(1, len(targets), 1):
        if criterion > targets[i][0]:
            continue # <==> pass
        elif criterion <= targets[i][0]:
            criterion = targets[i][1]
            answer += 1
            
    return answer
