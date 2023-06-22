# 문자열 압축

# my thoughts :
# 1. ....

from collections import deque

def solution(s):
    answer = list()

    for l in range(1, len(s) + 1, 1): # <<-- "문자열을 몇개 단위로 자를 것인가..??!!"
        queue = deque()
        
        for i in range(0, len(s), l):
            queue.append(s[i:i + l:1])
        
        # print(queue)
        # 출력결과 Ex : deque(['aab', 'bac', 'cc'])
    
        result = ""
        
        cur_str = queue.popleft()
        cur_cnt = 1
        
        while queue:
            temp = queue.popleft()
            
            if cur_str == temp:
                cur_cnt += 1
            else:
                if cur_cnt == 1:
                    result += cur_str
                else:
                    result += str(cur_cnt) + cur_str
                
                cur_str = temp
                cur_cnt = 1
        
        if cur_cnt == 1:
            result += cur_str
        else:
            result += str(cur_cnt) + cur_str
        
        answer.append(len(result))
    
    answer.sort()
    
    return answer[0]
