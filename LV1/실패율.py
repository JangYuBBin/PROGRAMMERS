# 실패율

from collections import defaultdict

def solution(N, stages):
    answer = []
    
    d = defaultdict(int)  
    for stage in stages:
        d[stage] += 1
    
    arr = list()
    
    total = len(stages) # <<-- "총 플레이어 수"
    
    for i in range(1, N + 1, 1):
        if total:
            arr.append((i, d[i] / total))
            total -= d[i]
        else:
            arr.append((i, 0)) # <<-- "스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의하기 때문입니다..!!"
    
    # print(arr)
    # 출력결과 Ex : 	[(1, 0.125), (2, 0.42857142857142855), (3, 0.5), (4, 0.5), (5, 0.0)]
    
    arr.sort(key = lambda x : (x[1], -x[0]), reverse = True)
    
    for num, val in arr:
        answer.append(num)

    return answer
