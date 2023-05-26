# 튜플

def solution(s):
    answer = []
    s = s[2:-2:1].split("},{")
    # print(s)
    # 출력결과 Ex : ['1,2,3', '2,1', '1,2,4,3', '2']
    s.sort(key = lambda x : len(x), reverse = False)
    # print(s)
    # 출력결과 Ex : ['3', '2,3', '4,2,3', '2,3,4,1']
    for i in range(0, len(s), 1):
        s[i] = s[i].split(",")
        # print(s[i])
        # 출력결과 Ex : ['4', '2', '3']
        s[i] = list(map(int, s[i]))
        # print(s[i])
        # 출력결과 Ex : [4, 2, 3]
    
    answer = s[0]
    
    for i in range(1, len(s), 1):
        for j in range(0, len(s[i]), 1):
            if s[i][j] not in answer:
                answer.append(s[i][j])
                break

    return answer
