# 옹알이(2)

def solution(babbling):
    answer = 0
    
    for i in range(0, len(babbling), 1):
        babbling[i] = babbling[i].replace("aya", "0")
        babbling[i] = babbling[i].replace("ye", "1")
        babbling[i] = babbling[i].replace("woo", "2")
        babbling[i] = babbling[i].replace("ma", "3")
    
    # print(babbling)
    # 출력결과 Ex : ['01', 'uuu', '11', '132', '00a']
    
    for i in range(0, len(babbling), 1):
        before = ""
        checkFlag = True
        
        for j in range(0, len(babbling[i]), 1):
            if babbling[i][j].isdigit():
                if not before:
                    before = babbling[i][j]
                else:
                    if before == babbling[i][j]:
                        checkFlag = False
                        break
                    else:
                        before = babbling[i][j]
            else:
                checkFlag = False
                break
        
        if checkFlag == True:
            answer += 1
        else:
            pass
    
    return answer
