# 쿼드압축 후 개수 세기

# my thoughts :
# 1. By using Recursion, We can solve it..!!

def solution(arr):
    global answer
    answer = [0, 0]

    def Recursion(start_v, l):
        global answer
    
        check = arr[start_v[0]][start_v[1]]
        checkFlag = True
    
        if l == 1:
            answer[check] += 1
            return
    
        for i in range(start_v[0], start_v[0] + l, 1):
            for j in range(start_v[1], start_v[1] + l, 1):
                if check != arr[i][j]:
                    checkFlag = False
                    break
                else:
                    pass
    
        if checkFlag == True:
            answer[check] += 1
        else:
            Recursion(start_v, l // 2)
            Recursion((start_v[0], start_v[1] + l // 2), l // 2)
            Recursion((start_v[0] + l // 2, start_v[1]), l // 2)
            Recursion((start_v[0] + l // 2, start_v[1] + l // 2), l // 2)
    
    Recursion((0, 0), len(arr))
    
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
