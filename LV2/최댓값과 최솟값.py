# 최댓값과 최솟값

def solution(s):
    answer = ''
    s = list(map(int, s.split()))
    s.sort()
    min = s[0]
    max = s[-1]
    answer = str(min) + " " + str(max)
    return answer
