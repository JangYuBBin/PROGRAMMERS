# 달리기 경주

# my thoughts :
# 1. 문자열 내장 함수인 .index()를 이용한다면 시간초과 판정을 받았습니다.
# 2. 시간초과를 피하기 위해 효율적으로 문제를 해결하는 방법을 생각해내야 합니다.
# 3. 시간초과를 피하기 위해서는 우리는 딕셔너리 자료형을 활용해야 합니다..!!
# 4. 틀린 문제이므로 다음에 다시 풀어보아야 할 문제인 것 같습니다..!!

def solution(players, callings):
    answer = []
    
    d = dict()
    for i, player in enumerate(players):
        d[player] = i # <<-- "인덱싱을 활용하기 위해 1등부터 부여하는 것이 아니라 0등부터 부여하는 방식을 선택합시다..!!"
    
    for calling in callings:
        d[calling] -= 1
        d[players[d[calling]]] += 1
        
        players[d[calling]], players[d[calling] + 1] = players[d[calling] + 1], players[d[calling]]
        
    answer = players
    
    return answer
