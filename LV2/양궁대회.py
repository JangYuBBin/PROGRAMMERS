# 양궁대회

# my thoughts :
# 1. 정확성 테스트가 10초이므로 중복조합 라이브러리를 활용할 수 있음.
# 2. info의 i번째 원소는 10 - i점을 맞힌 화살의 개수라는 점에 유의해야함.
# 3. 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법의 수가 여러가지일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return해야함.
# 4. 일단 도전해봅시다..!!

from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    
    cases = list(combinations_with_replacement([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], n))
    
    for case in cases:
        rian = [0] * 11
        # 참고 >  i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수입니다.
        
        for c in case:
            rian[10 - c] += 1
        
        # print(rian)
        # 출력결과 Ex : [0, 0, 1, 1, 0, 0, 0, 0, 2, 1, 0]

        score_r = 0
        score_a = 0

        for i in range(0, 10 + 1, 1):
            if rian[i] == info[i] == 0:
                continue
            elif rian[i] <= info[i]:
                score_a += 10 - i
            else:
                score_r += 10 - i
        
        if score_r > score_a:
            answer.append([score_r - score_a] + rian[-1::-1])
        
    answer.sort(reverse = True)

    if answer:
        return answer[0][1::1][-1::-1]
    else:
        return [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [0, 0, 1, 1, 0, 0, 0, 0, 2, 1, 0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
