# 방문 길이

def solution(dirs):
    answer = 0
    
    cur_v = (0, 0)
    
    already = set() # <<-- "여태까지 지나온 길을 기록하는 집합 자료형입니다..!!"
    
    for dir in dirs:
        if dir == "U":
            new_v = (cur_v[0], cur_v[1] + 1)
            
            if -5 <= new_v[0] <= 5 and -5 <= new_v[1] <= 5:
                pass
            else:
                continue
            
            already.add((new_v, cur_v))
            already.add((cur_v, new_v))
            
            cur_v = new_v
        elif dir == "D":
            new_v = (cur_v[0], cur_v[1] - 1)
            
            if -5 <= new_v[0] <= 5 and -5 <= new_v[1] <= 5:
                pass
            else:
                continue
                
            already.add((new_v, cur_v))
            already.add((cur_v, new_v))
            
            cur_v = new_v
        elif dir == "R":
            new_v = (cur_v[0] + 1, cur_v[1])
            
            if -5 <= new_v[0] <= 5 and -5 <= new_v[1] <= 5:
                pass
            else:
                continue
            
            already.add((new_v, cur_v))
            already.add((cur_v, new_v))
            
            cur_v = new_v
        elif dir == "L":
            new_v = (cur_v[0] - 1, cur_v[1])
            
            if -5 <= new_v[0] <= 5 and -5 <= new_v[1] <= 5:
                pass
            else:
                continue
            
            already.add((new_v, cur_v))
            already.add((cur_v, new_v))
            
            cur_v = new_v
    
    answer = len(already) // 2
        
    return answer
