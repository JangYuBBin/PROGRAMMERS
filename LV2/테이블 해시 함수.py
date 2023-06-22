# 테이블 해시 함수

# my thoughts :
# 1. 파이썬에서 bitwise XOR(Exclusive OR) 연산을 수행하기 위해서는 "^" 연산자를 사용하면 됩니다. "^" 연산자는 두 비트가 다를 때 1을 반환하고, 같을 때는 0을 반환합니다.
# 2. ....

def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key = lambda x : (x[col - 1], -x[0]), reverse = False)
    
    # print(data)
    # 출력결과 Ex : [[4, 2, 9], [2, 2, 6], [1, 5, 10], [3, 8, 3]]
    
    S_is = list()
    
    for i in range(row_begin - 1, row_end, 1):
        S_i = 0
        
        for j in range(0, len(data[i]), 1):
            S_i += data[i][j] % (i + 1)
        
        S_is.append(S_i)
    
    # print(S_is)
    # 출력결과 Ex : [0, 4]

    answer = S_is[0]

    for i in range(1, len(S_is), 1):
        answer = answer ^ S_is[i]
    
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))
