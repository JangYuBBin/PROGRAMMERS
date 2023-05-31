# 폰켓몬

def solution(nums):
    answer = 0
    
    n = len(nums) // 2
    
    d = dict()
    
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    
    arr = list()
    
    for k, v in d.items():
        arr.append((k, v))
        
    for k, v in arr:
        answer += 1
        n -= 1
        
        if n == 0:
            break
    
    return answer
