# [3차] n진수 게임

def From10Ton(num, n):
    answer = ""
    
    d = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9", 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F",}
    
    if num == 0:
        return "0"
    
    while num != 0:
        q, r = divmod(num, n)
        
        answer += d[r]
        
        num = q
    
    return answer[-1::-1]

def solution(n, t, m, p):
    answer = ""
    
    arr = ""
    for i in range(0, m * t + 1, 1): # <<-- "이 정도 범위만 되도 충분히 커버 가능..!!"
        arr += From10Ton(i, n)
    
    # print(arr)
    # 출력결과 Ex : ....
    
    idx = p - 1
    for _ in range(t):
        answer += arr[idx]
        idx += m
    
    return answer
