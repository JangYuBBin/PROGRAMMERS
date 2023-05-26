# 예상 대진표

# my thoughts :
# 1. 어떤수 a와 b(a < b)가 붙기 위해서는 다음의 조건을 만족해야 한다.
# 2. b - a == 1
# 3. a % 2 == 1
# 4. 또한 n번의 참가자가 승리한다면 다음 라운드에 부여 받을 번호는 다음과 같습니다.
# 5. next_n = cur_n // 2 + cur_n % 2

def solution(n,a,b):
    answer = 1
    
    while True:
        if abs(b - a) == 1 and min(a, b) % 2 == 1:
            return answer
        else:
            answer += 1
            a = a // 2 + a % 2
            b = b // 2 + b % 2
