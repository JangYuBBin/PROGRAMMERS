# 정수 제곱근 판별

from math import sqrt

def solution(n):
    if int(sqrt(n)) == sqrt(n):
        return (sqrt(n) + 1)**2
    else:
        return -1
