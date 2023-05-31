# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    
    cnt_0 = 0
    cnt_yes = 0
    
    for lotto in lottos:
        if lotto == 0:
            cnt_0 += 1
        elif lotto in win_nums:
            cnt_yes += 1
    
    max = cnt_0 + cnt_yes
    min = cnt_yes
    
    if max <= 1:
        answer.append(6)
    else:
        answer.append(7 - max)
    
    if min <= 1:
        answer.append(6)
    else:
        answer.append(7 - min)
    
    return answer
