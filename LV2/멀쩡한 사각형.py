# 멀쩡한 사각형

# my thoughts :
# 1. 약간의 센스가 필요했던 문제였습니다..!!

from math import gcd

def solution(w,h):
    return w * h - (w + h - gcd(w, h))
