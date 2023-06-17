# k진수에서 소수 개수 구하기

from math import sqrt

def IsPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num)) + 1 ,1):
            if num % i == 0:
                return False
            
        return True

def From10Tok(num, k):
    answer = ""
    
    while num != 0:
        q, r = divmod(num, k)
        
        answer += str(r)
        num = q
    
    return answer[-1::-1]

def solution(n, k):
    answer = 0
    
    num = From10Tok(n, k)
    nums = num.split("0")
    
    print(nums)
    
    for i in range(0, len(nums)):
        if nums[i] == "":
            continue
        else:
            pass
        
        if IsPrime(int(nums[i])):
            answer += 1
    
    return answer
