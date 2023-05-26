# 행렬의 곱셈

# my thoughts :
# 1. 다음에 다시 풀어볼만한 좋은 문제인 것 같습니다..!!

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    arr2 = list(map(list, zip(*arr2)))
    # print(arr2)
    # 출력결과 Ex : [[5, 2, 3], [4, 4, 1], [3, 1, 1]]
    
    for i in range(0, len(arr1), 1):
        for j in range(0, len(arr2), 1):
            val = 0
            for k in range(0, len(arr1[0]), 1):
                val += arr1[i][k] * arr2[j][k]
            
            answer[i][j] = val
    return answer
