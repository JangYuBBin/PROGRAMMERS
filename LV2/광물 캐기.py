# 광물 캐기

from itertools import permutations
from collections import deque

def solution(picks, minerals):
    answer = []
    
    arr = list()
    
    for pick, d_i_s in zip(picks, ["dia", "iron", "stone"]):
        arr.append((pick, d_i_s))
    
    # print(arr)
    # 출력결과 Ex : [(1, 'dia'), (3, 'iron'), (2, 'stone')]
    
    cases = list(permutations(arr, 3))
    
    # print(cases)
    # 출력결과 Ex : [((1, 'dia'), (3, 'iron'), (2, 'stone')), ((1, 'dia'), (2, 'stone'), (3, 'iron')), ((3, 'iron'), (1, 'dia'), (2, 'stone')), ((3, 'iron'), (2, 'stone'), (1, 'dia')), ((2, 'stone'), (1, 'dia'), (3, 'iron')), ((2, 'stone'), (3, 'iron'), (1, 'dia'))][((1, 'dia'), (3, 'iron'), (2, 'stone')), ((1, 'dia'), (2, 'stone'), (3, 'iron')), ((3, 'iron'), (1, 'dia'), (2, 'stone')), ((3, 'iron'), (2, 'stone'), (1, 'dia')), ((2, 'stone'), (1, 'dia'), (3, 'iron')), ((2, 'stone'), (3, 'iron'), (1, 'dia'))]
    
    for case in cases:
        picks = list()
        
        for pick, val in case:
            picks.extend([val] * pick)
        
        # print(picks)
        # 출력결과 Ex : ['dia', 'iron', 'iron', 'iron', 'stone', 'stone']
        
        pirodo = 0
        
        picks = deque(picks)
        
        copy_minerals = minerals[:]
        copy_minerals = deque(copy_minerals)
        
        while picks and copy_minerals:
            cur_pick = picks.popleft()
            cur_mineral = copy_minerals.popleft()
            
            if cur_pick == "dia":
                if cur_mineral == "dia":
                    pirodo += 1
                elif cur_mineral == "iron":
                    pirodo += 1
                elif cur_mineral == "stone":
                    pirodo += 1
            elif cur_pick == "iron":
                if cur_mineral == "dia":
                    pirodo += 5
                elif cur_mineral == "iron":
                    pirodo += 1
                elif cur_mineral == "stone":
                    pirodo += 1
            else:
                if cur_mineral == "dia":
                    pirodo += 25
                elif cur_mineral == "iron":
                    pirodo += 5
                elif cur_mineral == "stone":
                    pirodo += 1
        
        answer.append(pirodo)
        print(pirodo)
                
    answer.sort()
    
    return answer[0]

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
