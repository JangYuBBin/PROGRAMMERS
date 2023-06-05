# 이중우선순위큐

# another solution
# 풀이 참조 출처 : "https://chaewsscode.tistory.com/138"

# another thoughts :
# 1. 파이썬의 heapq는 최소힙만 지원하기 때문에 최대힙은 따로 구현해주어야 한다.
# 2. 최대 힙 구현을 위해 삽입 시 입력받은 숫자에 -1을 곱하고 결과값을 출력 시에는 -1을 다시 곱한 후 출력
# 3. 최대 힙, 최소 힙을 동기화 시켜주어야 한다.
# 4. 힙에 push 할 때 입력받은 값 num과 반복문이 몇 번 수행되었는지 가리키는 변수 i(즉, 인덱스 값)를 튜플 형태로 함께 넣어줌.
# 5. (파이썬의 튜플 비교연산은 첫 번째 원소를 기준으로 판단하기 때문에 힙의 구동에 영향 X)
# 6. 삭제 연산 시 id를 기준으로 해당 노드가 다른 힙에서 삭제된 노드인지 확인하기 위해 exists 플래그 리스트 사용
# 7. 이미 삭제된 노드인 경우 삭제되지 않은 노드가 나올 때까지 모두 버림
# 8. 삭제 대상 노드 등장 시 삭제
# 9. 모든 연산이 끝난 후에도 남아있는 동기화 되지 않은 노드가 있을 수 있기 때문에 각 힙의 False로 되어있는 값들은 버려주어 동기화 시킴.
# 10. 틀린 문제이기도 하고 매우 어려웠던 문제이므로 나중에 다시 풀어봐야 할 것 같습니다..!!

import heapq

def solution(operations):
    answer = [0, 0]

    min_h = []
    max_h = []

    exists = [False] * 1_000_000

    for i, operation in enumerate(operations):
        order, num = operation.split()
        num = int(num)

        if order == "I":
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            exists[i] = True
        elif order == "D":
            if num == 1:
                while max_h and exists[max_h[0][1]] == False:
                    heapq.heappop(max_h)
                if max_h:
                    exists[max_h[0][1]] = False
                    heapq.heappop(max_h)
            else:
                while min_h and exists[min_h[0][1]] == False:
                    heapq.heappop(min_h)
                if min_h:
                    exists[min_h[0][1]] = False
                    heapq.heappop(min_h)
        
    while min_h and not exists[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not exists[max_h[0][1]]:
        heapq.heappop(max_h)
    
    if max_h:
        answer[0] = -max_h[0][0]
    if min_h:
        answer[1] = min_h[0][0]

    return answer
