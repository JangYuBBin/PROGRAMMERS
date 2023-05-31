# 가장 가까운 같은 글자

# my thoughts :
# 1. By using 딕셔너리 자료형, We can solve it..!!

def solution(s):
    answer = []
    
    d = dict()
    
    for i, c in enumerate(s):
        if c not in d:
            answer.append(-1)
            d[c] = i
        else:
            answer.append(i - d[c])
            d[c] = i
    
    return answer

print(solution("banana"))
print(solution("foobar"))
