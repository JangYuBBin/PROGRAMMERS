# 뒤에 있는 큰 수 찾기

# my thoughts :
# 1. By using Stack, We can solve it..!!
# 2. 중요한 문제이므로 나중에 다시 풀어봐야 할 것 같습니다..!!

def solution(numbers):
    answer = [0] * len(numbers)
    
    stack = []
    
    for i, number in enumerate(numbers):
        if not stack:
            stack.append((i, number))
        elif stack:
            while stack and stack[-1][1] < number:
                idx, val = stack.pop()
                answer[idx] = number
            stack.append((i, number))
    
    while stack:
        idx, val = stack.pop()
        answer[idx] = -1
                    
    return answer
