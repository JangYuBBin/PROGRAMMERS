# 호텔 대실

# my thoughts :
# 1. By using Heap, We can solve it..!!
# 2. 대실 시작 시각, 대실 종료 시각을 분 기준으로 바꾼 후 waitings 리스트에 담는다.
# 3. waitings 리스트에 모두 담은 후 정렬을 해야한다. 이때 정렬 기준은 (대실 시작 시각, 대실 종료 시각) 기준으로 한다. 먼저 대실 되는 것을 고려하되 대실 시작 시각이 같다면 대실 종료 시각이 빠른 것을 우선적으로 고려해야 하기 때문이다. <<-- 이때 힙 자료구조를 활용하면 된다.
# 4. waitings 리스트의 원소를 하나씩 확인하면서 객실을 하나 더 마련해야 하는지 아니면 원래 사용하던 객실을 이어서 사용할 것인지 결정하면 됩니다..!!

import heapq

def solution(book_time):
    answer = 0

    waitings = []
    
    for i in range(0, len(book_time)):
        book_time[i][0] = list(map(int, book_time[i][0].split(":")))
        book_time[i][1] = list(map(int, book_time[i][1].split(":")))
        
        start = book_time[i][0][0] * 60 + book_time[i][0][1] # <<-- "대실 시작 시각을 분 형태로 변환..!!"
        end = book_time[i][1][0] * 60 + book_time[i][1][1] # <<-- "대실 종료 시각을 분 형태로 변환..!!"
        
        heapq.heappush(waitings, (start, end))
    
    start, end = heapq.heappop(waitings)

    rooms = []
    
    heapq.heappush(rooms, end)

    while waitings:
        start, end = heapq.heappop(waitings)

        if start >= rooms[0] + 10:
            heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        elif start < rooms[0] + 10:
            heapq.heappush(rooms, end)
    
    answer = len(rooms)
    
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
