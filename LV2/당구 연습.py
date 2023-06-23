# 당구 연습

# my thoughts :
# 1. 가장 중요한 점은 거리의 최솟값의 제곱을 구하는 문제이므로 "원쿠션"을 활용하여 목적지에 도달하는 것이 최소 거리일 것이라는 의심으로 문제에 접근해야 합니다..!!

def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        arr = list()
        
        endX = ball[0]
        endY = ball[1]
        
        # 먼저 x = ㅁ를 기준으로 원쿠션했을 때 거리를 구해봅시다.
        # x = 0
        if startY == endY and startX - endX > 0:
            pass
        else:
            new_endX = -endX
            new_endY = endY
            
            distance = (startX - new_endX)**2 + (startY - new_endY)**2
            
            arr.append(distance)
        
        # x = m
        if startY == endY and endX - startX > 0:
            pass
        else:
            new_endX = endX + 2 * (m - endX)
            new_endY = endY
            
            distance = (startX - new_endX)**2 + (startY - new_endY)**2
            
            arr.append(distance)
        
        # 그다음으로는 y = ㅁ를 기준으로 원쿠션했을 때 거리를 구해봅시다.
        # y = 0
        if startX == endX and startY - endY > 0:
            pass
        else:
            new_endX = endX
            new_endY = -endY
            
            distance = (startX - new_endX)**2 + (startY - new_endY)**2
            
            arr.append(distance)
        
        # y = n
        if startX == endX and endY - startY > 0:
            pass
        else:
            new_endX = endX
            new_endY = endY + 2 * (n - endY)
            
            distance = (startX - new_endX)**2 + (startY - new_endY)**2
            
            arr.append(distance)
        
        arr.sort(reverse = False)
        
        answer.append(arr[0])
    
    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
