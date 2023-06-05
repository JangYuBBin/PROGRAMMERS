# 베스트앨범

from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    d1 = dict() # <<-- "장르별로 재생된 횟수를 기록할 딕셔너리 자료형의 선언입니다..!!"
    d2 = defaultdict(list) # <<-- "장르별로 어떤 고유번호가 속해있는지 나타낼 딕셔너리 자료형의 선언입니다..!!"

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in d1:
            d1[genre] = play
        else:
            d1[genre] += play
        
        d2[genre].append((play, i))
        
    
    # print(d1)
    # 출력결과 Ex : {'classic': 1450, 'pop': 3100}
    # print(d2)
    # 출력결과 Ex : defaultdict(<class 'list'>, {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]})
    
    arr1 = list()
    for k, v in d1.items():
        arr1.append((k, v))
    arr1.sort(key = lambda x : x[1], reverse = True)
    
    for k in d2.keys():
        d2[k].sort(key = lambda x : (x[0], -x[1]), reverse = True)
    
    # print(arr1)
    # 출력결과 Ex : [('pop', 3100), ('classic', 1450)]
    # print(d2)
    # 출력결과 Ex : defaultdict(<class 'list'>, {'classic': [(800, 3), (500, 0), (150, 2)], 'pop': [(2500, 4), (600, 1)]})
    
    for k, v in arr1:
        if len(d2[k]) == 1:
            answer.append(d2[k][0][1])
        else:
            answer.append(d2[k][0][1])
            answer.append(d2[k][1][1])
        
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
