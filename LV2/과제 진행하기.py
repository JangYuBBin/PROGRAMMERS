# 과제 진행하기

# my thoughts :
# 1. 문제의 조건에 맞게 구현하면 되는 문제이지만 약간 어려웠던 것 같습니다..!!
# 2. 일단 배열이 시간 순으로 정렬되어 있지 않을 수 있으므로, 시간 순으로 정렬해줍니다.
# 3. 또한 Stack을 활용하여 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작하도록 합니다..!!
# 4. 중요한 문제이므로 나중에 다시 풀어봐야 할 것 같습니다..!!

def solution(plans):
    answer = []
    
    for i in range(0, len(plans), 1):
        plans[i][1] = plans[i][1].split(":")
        plans[i][1] = 60 * int(plans[i][1][0]) + int(plans[i][1][1])

        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x : x[1], reverse = False)
    
    cur_name = plans[0][0]
    cur_time = plans[0][1]
    remain = plans[0][2]
    
    stack = []
    
    i = 1
    while i <= len(plans) - 1:
        if cur_time + remain > plans[i][1]: # <<-- "새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작합니다."
            remain -= plans[i][1] - cur_time
            stack.append([cur_name, remain])
            
            cur_name = plans[i][0]
            cur_time = plans[i][1]
            remain = plans[i][2]
            
            i += 1
        elif cur_time + remain == plans[i][1]: # <<-- "만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다."
            answer.append(cur_name)
            
            cur_name = plans[i][0]
            cur_time = plans[i][1]
            remain = plans[i][2]
            
            i += 1
        elif cur_time + remain < plans[i][1]:
            answer.append(cur_name)
            
            if stack:
                cur_time += remain
                cur_name, remain = stack.pop()
            else:
                cur_time = plans[i][1]
                cur_name = plans[i][0]
                remain = plans[i][2]
                i += 1
                
    
    if stack:
        answer.append(cur_name)

        while stack:
            cur_name, remain = stack.pop()
            
            answer.append(cur_name)
    else:
        answer.append(cur_name)
    
    return answer

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	))
print(solution([["aaa", "12:00", "30"], ["bbb", "12:10", "30"], ["ccc", "14:00", "30"]]))
