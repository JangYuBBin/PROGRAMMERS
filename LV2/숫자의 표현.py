# 숫자의 표현

def solution(n):
    answer = 0
    
    for i in range(1, n + 1, 1):
        sum = i
        
        if sum == n:
            answer += 1
            break
        else:
            for j in range(i + 1, n + 1, 1):
                sum += j
                
                if sum < n:
                    pass
                elif sum == n:
                    answer += 1
                    break
                else:
                    break
                    
    return answer

print(solution(15))
print(solution(17))
