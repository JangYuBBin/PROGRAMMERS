# 이모티콘 할인행사

# my thoughts :
# 1. 결국 각 emoticon이 몇 퍼센트의 할인율을 갖느냐에 따라 결과가 다르게 나올 것입니다..!!
# 2. 중복순열 라이브러리를 활용하여 문제를 해결합시다..!!

from itertools import product

def solution(users, emoticons):
    answer = []
    
    cases = list(product([10, 20, 30, 40], repeat = len(emoticons)))
    # print(cases)
    # 출력결과 Ex : [(10, 10), (10, 20), (10, 30), (10, 40), (20, 10), (20, 20), (20, 30), (20, 40), (30, 10), (30, 20), (30, 30), (30, 40), (40, 10), (40, 20), (40, 30), (40, 40)]

    for case in cases:
        service = 0 # <<-- "이모티콘 플러스 서비스 가입자의 수"
        total = 0 # <<-- "모든 사용자의 비용의 합"
        
        for user in users:
            sum = 0 # <<-- "각 사용자마다 지불하게 될 비용"
            
            for i, emoticon in enumerate(emoticons):
                if case[i] >= user[0]: # <<-- "각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다."
                    sum += emoticon * (100 - case[i]) // 100
                else:
                    pass
            
            if sum >= user[1]:# <<-- "각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다."
                service += 1
            else:
                total += sum
        
        answer.append((service, total))
    
    answer.sort(key = lambda x : (x[0], x[1]), reverse = True)
    
    return [answer[0][0], answer[0][1]]
                
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
