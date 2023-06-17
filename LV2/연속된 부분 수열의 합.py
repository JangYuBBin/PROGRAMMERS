# 연속된 부분 수열의 합

# my thoughts :
# 1. Two Pointer를 활용하여 문제를 풀어보겠습니다..!!

def solution(sequence, k):
    answer = []
    
    start = 0
    end = 0
    sum = sequence[0]
    
    while True:
        if sum < k:
            end += 1
            
            if end > len(sequence) - 1:
                break
            else:
                sum += sequence[end]     
        elif sum == k:
            answer.append([start, end])
            
            sum -= sequence[start]
            start += 1
            
            if start > end:
                end = start
            else:
                pass
            
            if start > len(sequence) - 1:
                break
            else:
                pass
        elif sum > k:
            sum -= sequence[start]
            start += 1
            
            if start > end:
                end = start
            else:
                pass
    
    answer.sort(key = lambda x : (x[1] - x[0]), reverse = False)
    
    return answer[0]

print(solution([1, 2, 3, 4, 5],	7))
