# 괄호 회전하기

# my thoughts :
# 1. By using Stack, We can solve it..!!

def solution(s):
    answer = 0
    
    for x in range(0, len(s), 1):
        new_s = s[x::1] + s[0:x:1]
        
        stack = []
        
        checkFlag = True
        
        for c in new_s:
            if c == "(":
                stack.append(c)
            elif c == "[":
                stack.append(c)
            elif c == "{":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    checkFlag = False
                    break
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    checkFlag = False
                    break
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    checkFlag = False
                    break
        
        if stack:
            checkFlag = False
        else:
            pass
        
        if checkFlag == True:
            answer += 1
        else:
            pass
    
    return answer
