# 연속 부분 수열 합의 개수

# my thoughts :
# 1. By using Brute Force, We can solve it..!!

def solution(elements):
    answer = set()
    
    l = len(elements)

    elements += elements
    
    # print(elements)
    # 출력결과 Ex : [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    # -->> "인덱싱 오류를 발생시키지 않기 위해 이렇게 리스트를 변경해줍시다..!!"
    
    for i in range(1, l + 1, 1): # <<-- "길이가 i인 연속 부분 수열"
        for j in range(0, l, 1):
            temp = elements[j:j + i:1]
            
            answer.add(sum(temp))
    
    return len(answer)

print(solution([7, 9, 1, 1, 4]))
