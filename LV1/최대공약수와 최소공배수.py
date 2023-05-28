# 최대공약수와 최소공배수

from math import gcd

def solution(n, m):
    answer = [0, 0]
    answer[0] = gcd(n, m)
    answer[1] = answer[0] * (n // answer[0]) * (m // answer[0])
    return answer
