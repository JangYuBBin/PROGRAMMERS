# 자연수를 뒤집어 배열로 만들기

def solution(n):
    return list(map(int, list(str(n)[-1::-1])))
