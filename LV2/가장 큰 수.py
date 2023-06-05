# 가장 큰 수

# functools 라이브러리의 cmp_to_key() 함수 설명 참조 출처 : "https://wikidocs.net/109303"

# my thoughts :
# 1. 틀린 문제이므로 나중에 다시 풀어보아야 할 문제인 것 같습니다..!!
# 2. 색다른 풀이를 발견해서 정리하려고 합니다.
# 3. 이 풀이는 functools 라이브러리의 cmp_to_key 함수를 사용한 풀이입니다.
# 4. 여기서 functools 라이브러리의 cmp_to_key() 함수는..??
# 5. functools.cmp_to_key(func)는 sorted()와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는 함수입니다. 단, func() 함수는 두 개의 인수를 입력하여 첫 번째 인수를 기준으로 그 둘을 비교하여 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수이어야 합니다.
# "관련 문제 Ex"
# 다음과 같이 2차원 평면의 점 N개를 (x, y)좌표로 구성한 리스트가 있다. y좌표가 증가하는 순으로 y 좌표가 같으면 x좌표가 증가하는 순으로 좌표를 정렬하고 이를 출력하는 프로그램을 만들려면 어떻게 해야 할까?
# [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
# 즉, 정렬 후에는 다음과 같은 결과를 출력해야 한다.
# [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]
# "풀이"
# 이 문제는 sorted() 함수의 두 번째 key 매개변수에 특별한 방법으로 정렬할 수 있는 함수를 전달하여 해결해야 한다. key에 함수를 전달하려면 다음처럼 functools.cmp_to_key()를 사용한다.
# "code"
"""
import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]: # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]: # y 좌표가 같다면
        if n1[0] > n2[0]: # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]: # x 좌표가 같다면
            return 0
        else:
            return -1
    else: # y 좌표가 작다면
        return -1

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key = functools.cmp_to_key(xy_compare))
print(result)
"""

import functools

def compare(num1, num2):
    result1 = num1 + num2
    result2 = num2 + num1
    
    if int(result1) > int(result2):
        return 1
    elif int(result1) == int(result2):
        return 0
    else:
        return -1

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = functools.cmp_to_key(compare), reverse = True)
    answer = "".join(numbers)
    if answer == "0" * len(answer): # <<-- "예외 상황을 처리해줍시다..!!"
        return "0"
    return answer
