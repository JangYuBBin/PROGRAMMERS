# 다리를 지나는 트럭

# my thoughts :
# 1. 스택과 큐에 관한 좋은 문제이므로 나중에 다시 풀어보도록 합시다..!!

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0] * bridge_length # <<-- "예를 들어, 트럭 2대가 올라갈 수 있고 ...."
    bridge = deque(bridge)
    sum = 0
    
    truck_weights = deque(truck_weights)
    
    while True:
        answer += 1
        
        if truck_weights:
            sum -= bridge.popleft()
            
            if sum + truck_weights[0] <= weight:
                sum += truck_weights[0]
                bridge.append(truck_weights[0])
                truck_weights.popleft()
            else:
                bridge.append(0)
        else:
            bridge.popleft()
        
        if not bridge:
            return answer
