# 다음 큰 숫자

def solution(n):
    answer = 0
    check = (bin(n)[2:]).count("1")
    num = n + 1
    while True:
        bin_num = bin(num)[2:]
        if bin_num.count("1") == check:
            answer = num
            break
        else:
            num += 1
    return answer
