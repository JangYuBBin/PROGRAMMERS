# 단어 변환

# my thoughts :
# 1. By using Dijkstra + BFS Algorithm, We can solve it..!!
# 2. 중요한 문제이니 다음에 또 풀어보도록 합시다..!!

from collections import defaultdict
from collections import deque

def solution(begin, target, words):
    answer = 0
    
    l = len(begin) # <<-- "각 단어의 길이"
    
    graph = defaultdict(list)
    for begin in [begin]:
        for word in words:
            cnt = 0
            
            for i in range(0, l, 1):
                if begin[i] != word[i]:
                    cnt += 1
                else:
                    pass
            
            if cnt == 1:
                graph[begin].append(word)
            else:
                pass
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if i == j:
                continue
            else:
                pass
            
            cnt = 0
            
            for k in range(0, l, 1):
                if words[i][k] != words[j][k]:
                    cnt += 1
                else:
                    pass
                
            if cnt == 1:
                graph[words[i]].append(words[j])
            else:
                pass
    
    # print(graph)
    # 출력결과 Ex : defaultdict(<class 'list'>, {'hit': ['hot'], 'hot': ['dot', 'lot'], 'dot': ['hot', 'dog', 'lot'], 'dog': ['dot', 'log', 'cog'], 'lot': ['hot', 'dot', 'log'], 'log': ['dog', 'lot', 'cog'], 'cog': ['dog', 'log']})
    
    costs = dict()
    costs[begin] = float("inf")
    costs[target] = float("inf")
    for word in words:
        costs[word] = float("inf")
    
    costs[begin] = 0

    queue = deque()

    queue.append(begin)

    while queue:
        cur_v = queue.popleft()

        for new_v in graph[cur_v]:
            if costs[new_v] > costs[cur_v] + 1:
                costs[new_v] = costs[cur_v] + 1
                queue.append(new_v)
    
    if costs[target] == float("inf"):
        return 0
    else:
        return costs[target]

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
