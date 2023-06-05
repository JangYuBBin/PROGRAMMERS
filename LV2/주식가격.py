# 주식가격

# my thoughts :
# 1. 다음에 다시 풀어보아야 할 문제 중 하나인 것 같습니다..!!
# 2. 그런데 왜 이게 스택/큐 문제인지..??

def solution(prices):
    answer = []
    
    for i in range(0, len(prices)):
        sec = 0
        
        for j in range(i + 1, len(prices)):
            sec += 1
            
            if prices[i] > prices[j]:
                break
            else:
                pass
        
        answer.append(sec)
            
    return answer
