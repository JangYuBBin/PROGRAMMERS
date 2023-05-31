# 명예의 전당 (1)

# my thoughts :
# 1. ....

def solution(k, score):
    answer = []
    
    arr = []
    
    for s in score:
        if len(arr) < k:
            arr.append(s)
            arr.sort()
        elif len(arr) >= k:
            arr.append(s)
            arr.sort()
            arr = arr[1::1]
        
        answer.append(arr[0])
        
    return answer
