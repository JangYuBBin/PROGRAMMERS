# N개의 최소공배수 

# my thoughts :
# 1. By using Brute Force, We can solve it..!!

from math import gcd

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr), 1):
        temp = gcd(answer, arr[i])
        
        answer = temp * (answer // temp) * (arr[i] // temp)
    return answer
