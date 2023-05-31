# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):
        arr1[i] = bin(arr1[i])[2:]
        
        if len(arr1[i]) < n:
            arr1[i] = "0" * (n - len(arr1[i])) + arr1[i]
    
    for i in range(0, n):
        arr2[i] = bin(arr2[i])[2:]
        
        if len(arr2[i]) < n:
            arr2[i] = "0" * (n - len(arr2[i])) + arr2[i]
    
    # print(arr1)
    # print(arr2)
    # 출력결과 Ex : ['01001', '10100', '11100', '10010', '01011']
    # ['11110', '00001', '10101', '10001', '11100']
    
    for i in range(0, n):
        temp = ""
        
        for j in range(0, n):
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                temp += "#"
            else:
                temp += " "
        
        answer.append(temp)
    
    return answer
