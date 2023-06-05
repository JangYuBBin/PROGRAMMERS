# 여행경로

# my thoughts :
# 1. 중요한 문제이므로 나중에 다시 풀어봐야 할 것 같습니다..!!
# 2. By using DFS + Backtracking Algorithm, We can solve it..!!
# 3. 참고로 answer.append(result) 대신 answer.append(result.copy()) 코드를 사용해야 합니다.
# 4. 그 이유는 다음과 같습니다.
# 5. answer.append(result) 코드를 사용한다면 result 리스트 자체를 answer 리스트에 추가하는 것입니다. 이 경우 result 리스트는 answer 리스트에 대한 참조가 되므로, result 리스트의 내용이 변경되면 answer 리스트에도 영향을 줍니다. 즉, result 리스트를 추가한 이후에 result 리스트를 변경하면 answer 리스트에도 반영됩니다.

import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    for a, b in tickets:
        graph[a].append(b)
    
    for k in graph.keys():
        graph[k].sort()
    
    result = ["ICN"]

    def dfs():
        if len(result) == len(tickets) + 1:
            answer.append(result.copy())
            return
        else:
            for new_v in graph[result[-1]]:
                result.append(new_v)
                graph[result[-2]].remove(result[-1]) # <<-- "반복문을 도는 중에 리스트를 변경할 시 위험할 수 있다는 점을 항상 염두에 두어야 합니다..!!"

                dfs()

                graph[result[-2]].append(result[-1])
                graph[result[-2]].sort()
                result.pop()

    dfs()

    answer.sort()
    
    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) 
