# 모의고사

# my thoughts :
# 1. 1번 수포자 패턴 : [1, 2, 3, 4, 5], 길이는 5
# 2. 2번 수포자 패턴 : [2, 1, 2, 3, 2, 4, 2, 5], 길이는 8
# 3. 3번 수포자 패턴 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 길이는 10

def solution(answers):
    answer = []
    
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(0, len(answers), 1):
        if answers[i] == arr1[i % 5]:
            cnt_1 += 1
        
        if answers[i] == arr2[i % 8]:
            cnt_2 += 1
        
        if answers[i] == arr3[i % 10]:
            cnt_3 += 1
    
    check = [(1, cnt_1), (2, cnt_2), (3, cnt_3)]
    check.sort(key = lambda x : x[1], reverse = True)
    
    for i in range(0, 3, 1):
        if check[i][1] != check[0][1]:
            break
        else:
            answer.append(check[i][0])
    
    answer.sort()
        
    return answer
