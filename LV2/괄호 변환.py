# 괄호 변환

# my thoughts :
# 1. 문제의 설명에 맞게 구현..!!

def solution(p):
    answer = ''
    
    def function(w):
        # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        if not w:
            return w
        else:
            pass
        
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
        u = ""
        v = ""
        plus_or_minus = 0
        
        for i in range(0, len(w), 1):
            if w[i] == "(":
                u += w[i]
                
                plus_or_minus += 1
            else:
                u += w[i]
                
                plus_or_minus -= 1
            
            if plus_or_minus == 0:
                v = w[i+1::1]
                break
        
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        checkFlag = True
        stack = []

        for c in u:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    checkFlag = False
                    break
        
        if stack:
            checkFlag = False
        else:
            pass

        if checkFlag == True:
            u += function(v)

            return u
        else:
            pass

        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        empty = ""
        empty += "("
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        empty += function(v)
        # 4-3. ')'를 다시 붙입니다. 
        empty += ")"
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = u[1:len(u) - 1:1]

        new_u = ""

        for c in u:
            if c == "(":
                new_u += ")"
            else:
                new_u += "("
        
        empty += new_u

        return empty
    
    return function(p)

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
