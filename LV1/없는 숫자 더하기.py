# 없는 숫자 더하기

def solution(numbers):
    answer = 0
    
    for i in range(0, 9 + 1, 1):
        if i not in numbers:
            answer += i
            
    return answer
