# 짝지어 제거하기

# my thoughts :
# 1. By using Stack, We can solve it..!!

def solution(s):
    stack = []
    
    for c in s:
        stack.append(c)
        
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    if stack:
        return 0
    else:
        return 1
