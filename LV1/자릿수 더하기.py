# 자릿수 더하기

def solution(n):
    answer = 0
    for c in str(n):
        answer += int(c)
    return answer
