# 햄버거 만들기

# my thoughts :
# 1. 1 : 빵
# 2. 2 : 야채
# 3. 3 : 고기
# 4. 즉, 햄버거를 만들기 위해서는 1 - 2 - 3 - 1 순이어야 합니다..!!
# 5. By using Stack, We can solve it..!!

def solution(ingredient):
    answer = 0
    
    stack = []
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            
            answer += 1
            
    return answer
