# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [x + x * i for i in range(0, n, 1)]
