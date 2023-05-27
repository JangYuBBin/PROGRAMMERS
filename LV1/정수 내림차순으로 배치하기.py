# 정수 내림차순으로 배치하기

def solution(n):
    arr = list(str(n))
    arr.sort(reverse = True)
    return int("".join(arr))
