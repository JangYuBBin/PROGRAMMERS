# 구명보트

# my thoughts :
# 1. people 리스트를 내림차순으로 정렬하고 큐 자료구조로 바꾼다.
# 2. 일단 현재 무인도에 갇힌 사람 중 몸무게가 가장 많이 나가는 people[0]이 limit와 같은지 혹은 작은지 확인한다.
# 3. limit과 같다면 혼자 태워서 보낸다.
# 4. limit보다 작다면 현재 무인도에 갇힌 사람 중 몸무게가 가장 적게 나가는 people[-1]도 같이 태워서 보낼 수 있는지 확인한다.
# 5. 무인도에 갇힌 사람이 없을 때까지 반복한다.

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    people = deque(people)
    
    while people:
        big = people.popleft()
        if big < limit:
            if people and people[-1] + big <= limit:
                small = people.pop()
                answer += 1
            else:
                answer += 1
        else: # <<==>> "big == limit:"
            answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
