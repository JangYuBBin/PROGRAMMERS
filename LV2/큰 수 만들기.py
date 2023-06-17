# 큰 수 만들기

# my thoughts :
# 1. By using Stack, We can solve it..!!

def solution(number, k):
    answer = ''
    
    stack = []
    
    for num in number:
        if not stack:
            stack.append(num)
        elif stack:
            while stack and stack[-1] < num and k > 0:
                stack.pop()
                k -= 1
            stack.append(num)
    
    if k:
        while k:
            stack.pop()
            k -= 1
    
    answer = "".join(stack)
            
    return answer
