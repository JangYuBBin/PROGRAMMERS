# 시소 짝꿍

# my thoughts :
# 1. 단순히 2중 반복문을 활용한다면 시간초과 판정을 받을 것입니다..!!
# 2. 따라서 딕셔너리 자료형을 활용하여 문제를 해결해봅시다..!!
# 3. 이전 코드에서 문제가 발생했던 부분은 조건문의 비교 연산자였습니다. 부동소수점 비교는 정확한 결과를 내지 못할수도 있습니다. 따라서 문제가 발생했던 것으로 보입니다. 대신에 정수 연산을 통해 조건을 처리해야 합니다..!!

def solution(weights):
    answer = 0

    d = dict()

    for weight in weights:
        if weight in d:
            d[weight] += 1
        else:
            d[weight] = 1

    arr = list(d.keys())
    arr.sort()

    for i in range(0, len(arr) - 1, 1):
        for j in range(i + 1, len(arr), 1):
            if arr[j] * 2 == arr[i] * 3:
                answer += d[arr[j]] * d[arr[i]]
            elif arr[i] * 2 == arr[j]:
                answer += d[arr[j]] * d[arr[i]]
            elif arr[j] * 3 == arr[i] * 4:
                answer += d[arr[j]] * d[arr[i]]

    for val in arr:
        if d[val] >= 2:
            answer += (d[val] * (d[val] - 1)) // 2

    return answer
