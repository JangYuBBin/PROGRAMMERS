# 문자열 나누기

# my thoughts :
# 1. By using Stack, We can solve it..!!

def solution(s):
    answer = 0
    
    stack = []
    
    criterion = s[0]
    
    for i in range(0, len(s), 1):
        if criterion == "":
            criterion = s[i]
            
        if s[i] == criterion:
            stack.append(s[i])
        else:
            stack.pop()
        
        if not stack:
            answer += 1
            criterion = ""
        else:
            pass
    
    if stack:
        answer += 1
            
    return answer
