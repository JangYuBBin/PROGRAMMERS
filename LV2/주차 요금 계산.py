# 주차 요금 계산

from collections import defaultdict

def solution(fees, records):
    answer = []
    
    d = defaultdict(int) # <<-- "각 차량마다 주차장에 있었던 시간을 기록할 딕셔너리 자료형의 선언입니다..!!"
    check = dict() # <<-- "각 차량마다 현재 주차장에 있는지 없는지를 나타낼 딕셔너리 자료형의 선언입니다..!!"
    
    for record in records:
        record = record.split()
        
        time = record[0]
        time = time.split(":")
        time = int(time[0]) * 60 + int(time[1]) # 현재 시각
        number = record[1] # 차량 번호
        in_or_out = record[2] # 들어가는가 나오는가..!!
        
        check[number] = in_or_out
        
        if check[number] == "IN":
            d[number] -= time
        else:
            d[number] += time
    
    for k in check.keys():
        if check[k] == "IN":
            d[k] += 23 * 60 + 59
        else:
            pass
        
    numbers = list(d.keys())
    numbers.sort()
    
    for number in numbers:
        val = 0
        
        if d[number] <= fees[0]:
            val += fees[1]
            answer.append(val)
        else:
            val += fees[1]
            
            diff = d[number] - fees[0]
            
            q, r = divmod(diff, fees[2])
            
            if r == 0:
                diff = q
            else:
                diff = q + 1
            
            val += diff * fees[3]
            
            answer.append(val)
            
    return answer
