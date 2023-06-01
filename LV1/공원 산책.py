# 공원 산책

# my thoughts :
# 1. 문제에 조건에 맞게 구현하면 되는 구현문제인 것 같습니다..!!

def solution(park, routes):
    answer = []
    
    cur_v = [0, 0]
    for i in range(0, len(park)):
        for j in range(0, len(park[0])):
            if park[i][j] == "S":
                cur_v[0] = i
                cur_v[1] = j
                break
    # print(cur_v)
    # 출력결과 Ex : [0, 0]

    before_v = cur_v[:] # <<-- "route가 불가능한 route일때를 대비하여..!!"
    
    for route in routes:
        d, cnt = route.split()
        cnt = int(cnt)

        if d == "N": # 북쪽
            # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
            if 0 <= cur_v[0] - cnt < len(park) and 0 <= cur_v[1] < len(park[0]):
                pass
            else:
                continue
                
            # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
            checkFlag = True
            
            for _ in range(cnt):
                cur_v = [cur_v[0] - 1, cur_v[1]]
                
                if park[cur_v[0]][cur_v[1]] != "X":
                    pass
                else:
                    checkFlag = False
                    break
            
            if checkFlag == True:
                before_v = cur_v[:]
            else:
                cur_v = before_v[:]
                continue
        elif d == "S": # 남쪽
            # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
            if 0 <= cur_v[0] + cnt < len(park) and 0 <= cur_v[1] < len(park[0]):
                pass
            else:
                continue
                
            # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
            checkFlag = True
            
            for _ in range(cnt):
                cur_v = [cur_v[0] + 1, cur_v[1]]
                
                if park[cur_v[0]][cur_v[1]] != "X":
                    pass
                else:
                    checkFlag = False
                    break
            
            if checkFlag == True:
                before_v = cur_v[:]
            else:
                cur_v = before_v[:]
                continue
        elif d == "W": # 서쪽
            # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
            if 0 <= cur_v[0] < len(park) and 0 <= cur_v[1] - cnt < len(park[0]):
                pass
            else:
                continue
                
            # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
            checkFlag = True
            
            for _ in range(cnt):
                cur_v = [cur_v[0], cur_v[1] - 1]
                
                if park[cur_v[0]][cur_v[1]] != "X":
                    pass
                else:
                    checkFlag = False
                    break
            
            if checkFlag == True:
                before_v = cur_v[:]
            else:
                cur_v = before_v[:]
                continue
        elif d == "E": # 동쪽
            # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
            if 0 <= cur_v[0] < len(park) and 0 <= cur_v[1] + cnt < len(park[0]):
                pass
            else:
                continue
                
            # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
            checkFlag = True
            
            for _ in range(cnt):
                cur_v = [cur_v[0], cur_v[1] + 1]
                
                if park[cur_v[0]][cur_v[1]] != "X":
                    pass
                else:
                    checkFlag = False
                    break
            
            if checkFlag == True:
                before_v = cur_v[:]
            else:
                cur_v = before_v[:]
                continue
    
    answer = cur_v

    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
