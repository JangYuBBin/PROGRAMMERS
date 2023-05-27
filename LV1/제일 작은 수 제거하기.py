# 제일 작은 수 제거하기

def solution(arr):
    arr.remove(min(arr))
    
    if not arr:
        return [-1]
    else:
        return arr
