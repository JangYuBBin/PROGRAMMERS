# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]
    
    while True:
        if s == "1":
            break
        else:
            answer[1] += s.count("0")
            s = s.replace("0", "")
            answer[0] += 1
            s = bin(len(s))[2:]
    return answer

print(solution("110010101001"))
