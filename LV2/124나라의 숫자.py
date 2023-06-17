# 124나라의 숫자

# my thoughts :
# 1. 124 나라는 3개의 숫자 1, 2, 4로 숫자를 표현
# 2. 이는 3진법과 유사 -->> 즉, 3진법을 활용하여 문제를 해결해야 한다.
# 3. n을 3으로 나누었을 때 나머지가 1, 2이면 그대로.
# 4. n을 3으로 나누었을 때 나머지가 0이면 "4"를 answer에 더하고 몫 -= 1 처리
# 5. n이 0이 될 때까지 이 행동을 반복하고 끝나면 answer = answer[-1::-1] 처리
# 6. 틀린 문제이므로 나중에 다시 풀어봐야 할 것 같습니다..!!

def solution(n):
    answer = ''
    
    while n != 0:
        q, r = divmod(n, 3)
        
        if r == 0:
            answer += str(4)
            q -= 1
            n = q
        else:
            answer += str(r)
            n = q
    
    answer = answer[-1::-1]
    
    return answer
