# 스킬트리

# my thoughts :
# 1. By using Stack, We can solve it..!!

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        checkFlag = True
        
        stack = list(skill)[-1::-1]
        
        for c in skill_tree:
            if c in stack:
                if c == stack[-1]:
                    stack.pop()
                else:
                    checkFlag = False
                    break
            else:
                pass
            
            if not stack:
                break
        
        if checkFlag == True:
            answer += 1
        else:
            pass
        
    return answer
