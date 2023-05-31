# 대충 만든 자판

def solution(keymap, targets):
    answer = []
    
    d = dict()
    
    for i in range(0, len(keymap), 1):
        for j in range(0, len(keymap[i]), 1):
            if keymap[i][j] not in d:
                d[keymap[i][j]] = j + 1
            else:
                d[keymap[i][j]] = min(j + 1, d[keymap[i][j]])
    
    for target in targets:
        val = 0
        checkFlag = True
        
        for c in target:
            if c not in d:
                checkFlag = False
                break
                
            val += d[c]
        
        if checkFlag == True:
            answer.append(val)
        else:
            answer.append(-1)
            
    return answer
