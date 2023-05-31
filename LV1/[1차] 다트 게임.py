# [1차] 다트 게임

def solution(dartResult):
    stack = []
    
    scores = []
    
    cur_score = ""
    for i in range(0, len(dartResult), 1):
        if i == len(dartResult) - 1:
            cur_score += dartResult[i]
            scores.append(cur_score)
            cur_score = ""
        elif dartResult[i].isalpha() and dartResult[i + 1].isdigit():
            cur_score += dartResult[i]
            scores.append(cur_score)
            cur_score = ""
        elif dartResult[i] in ["#", "*"] and dartResult[i + 1].isdigit():
            cur_score += dartResult[i]
            scores.append(cur_score)
            cur_score = ""
        else:
            cur_score += dartResult[i]
        
    # print(scores)
    # 출력결과 Ex : ['1S*', '2T*', '3S']
    
    for score in scores:
        val = ""
        
        for s in score:
            if s.isdigit():
                val += s
            elif s.isalpha():
                val = int(val)
                
                if s == "S":
                    val = val**1
                elif s == "D":
                    val = val**2
                elif s == "T":
                    val = val**3
            else:
                if s == "*":
                    if stack:
                        stack[-1] *= 2
                        val *= 2
                    else:
                        val *= 2
                elif s == "#":
                    val *= -1
        
        stack.append(val)
    
    return sum(stack)


print(solution("1S2D*3T"))
