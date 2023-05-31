# 크기가 작은 부분문자열

def solution(t, p):
    answer = 0
    
    for i in range(0, len(t) - len(p) + 1, 1):
        num = int(t[i:i + len(p):1])
        
        if num <= int(p):
            answer += 1
            
    return answer

print(solution("10203", "15"))
