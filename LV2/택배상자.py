# 택배상자

# my thoughts :
# 1. By using Stack and Queue, We can solve it..!!

from collections import deque

def solution(order):
    answer = 0
    
    main = deque(list(range(1, len(order) + 1, 1))) # <<-- "Queue의 자료구조를 갖는 자료형입니다..!!"
    sub = [] # <<-- "Stack의 자료구조를 갖는 자료형입니다..!!"
    
    for o in order:
        while main and main[0] < o:
            sub.append(main.popleft())
        
        if main and main[0] == o:
            main.popleft()
            answer += 1
        elif sub and sub[-1] == o:
            sub.pop()
            answer += 1
        else:
            break
    
    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
