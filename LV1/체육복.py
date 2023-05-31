# 체육복

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * n
    
    for i in lost:
        students[i - 1] -= 1
    
    for i in reserve:
        students[i - 1] += 1
        
    # print(students)
    # 출력결과 Ex : [2, 0, 2, 0, 2]
    
    for i in range(0, len(students), 1):
        if i == 0:
            if students[i] == 2 and students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1
        elif i == n - 1:
            if students[i] == 2 and students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
        else:
            if students[i] == 2 and students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
            elif students[i] == 2 and students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1
    
    for student in students:
        if student >= 1:
            answer += 1
        else:
            pass
        
    return answer
