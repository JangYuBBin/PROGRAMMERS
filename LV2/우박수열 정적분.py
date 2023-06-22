# 우박수열 정적분

def solution(k, ranges):
    answer = []
    
    arr = list()
    
    arr.append(k)
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        
        arr.append(k)
    
    # print(arr)
    # 출력결과 Ex : [5, 16, 8, 4, 2, 1]
    
    for start, end in ranges:
        end = len(arr) - 1 + end
        
        if start > end:
            answer.append(-1.0)
        else:
            val = 0.0
            
            for i in range(start, end, 1):
                val += (arr[i] + arr[i + 1]) / 2
            
            answer.append(val)
    
    return answer
