# 두 큐 합 같게 만들기

# my thoughts :
# 1. queue1을 기준으로 보았을 때 다시 queue1 원래대로 돌아올려면 총 len(queue1) * 4번 수행해야 한다.
# 2. 따라서 len(queue1) * 4번 작업을 수행할 동안 두 큐의 합이 같아지지 않는다면 그 경우는 불가능한 경우입니다.
# 3. 또한 작업을 시작하기전 두 큐의 합이 홀수라면 애초에 2로 나누어지지 않는 상황이므로 그 경우도 불가능한 상황입니다.
# 4. 이 점을 고려하여 작업을 수행하면 될 것입니다..!!

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    l = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    check = sum(queue1) + sum(queue2) 
    
    if check % 2 == 1: # <<-- "두 큐의 전체 합이 홀수라면 2로 나눌수 없으므로 애초에 불가능한 상황입니다. 따라서 -1을 return 해줍시다..!!"
        return -1 
    else:
        check //= 2
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt = 0
    while cnt <= l * 4:
        if sum1 == check:
            return cnt
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        elif sum1 > sum2:
            sum2 += queue1[0]
            sum1 -= queue1[0]
            queue2.append(queue1.popleft())
        
        cnt += 1
        

    return -1

print(solution([1, 2, 1, 2],	[1, 10, 1, 2]))
