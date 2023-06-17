# 2개 이하로 다른 비트

# my thoughts :
# 1. 만약 x를 2진수로 바꾼 수의 표현에서 0이 없을 경우 111 -->> 1011 이런 식으로 자릿수를 하나 늘리고 첫 자릿수에 1 그다음 자릿수에 0을 그리고 그 다음엔 똑같이 대입해줍니다.
# 2. 만약 x를 2진수로 바꾼 수의 표현에서 0이 있을 경우 가장 마지막에 나타나는 0을 1로 바꿔주고 그 다음에 해줄 액션은 다음과 같습니다.
# 3. 1로 바꾼 자리 다음부터 나타나는 1 하나를 0으로 바꿔줍니다.
# 3. 위의 규칙을 활용하여 문제를 풀어봅시다..!!

def f(x):
    answer = ""
    
    bin_x = list(bin(x)[2:])
    
    idx = -1 # <<-- "x를 2진수로 표현했을 때 가장 늦게 나타나는 0의 idx를 표시하기 위한 변수입니다..!!"
    
    for i in range(len(bin_x) - 1, -1, -1):
        if bin_x[i] == "0":
            idx = i
            break
        else:
            pass
        
    if idx == -1: # <<-- "만약 x를 2진수로 표현한 수에서 0이 없을 경우입니다..!!"
        answer = ["1"] + ["0"] + bin_x[1::1]
        
        answer = int("".join(answer), 2)
        
        return answer
    else:
        answer = bin_x[0:idx:1] + ["1"] + bin_x[idx + 1::1]
    
        for i in range(idx + 1, len(answer), 1):
            if answer[i] == "1":
                answer[i] = "0"
                break
            else:
                pass
    
        answer = int("".join(answer), 2)
        
        return answer

def solution(numbers):
    answer = []
    
    for number in numbers:
        answer.append(f(number))
    
    return answer
