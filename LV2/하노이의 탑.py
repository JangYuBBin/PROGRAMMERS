# 하노이의 탑

# my thoughts :
# 1. By using Recursion, We can solve it..!!

def solution(n):
    answer = []
    
    def Hanoi(start, end, by, n):
        if n == 1:
            return [[start, end]]
        else:
            return Hanoi(start, by, end, n - 1) + [[start, end]] + Hanoi(by, end, start, n - 1)
    
    answer = Hanoi(1, 3, 2, n)
    
    return answer

print(solution(2))
