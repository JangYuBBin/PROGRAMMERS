# 핸드폰 번호 가리기

def solution(phone_number):
    l = len(phone_number)
    answer = "*" * (l - 4)
    
    if l >= 4:
        answer += phone_number[-4::1]
    
    return answer
