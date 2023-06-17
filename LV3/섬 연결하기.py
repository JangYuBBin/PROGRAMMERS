# 섬 연결하기

# my thoughts :
# 1. By using MST(최소 스패닝 트리), We can solve it..!!

def solution(n, costs):
    answer = 0
    
    def find_parent(parent, x):
        if parent[x] != x: # 루트 노드가 아니라면
            parent[x] = find_parent(parent, parent[x])
        else:
            pass
        
        return parent[x]
    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    parent = [0] * n 
    for i in range(0, n, 1):
        parent[i] = i
    
    costs.sort(key = lambda x : x[2], reverse = False)
    
    for v1, v2, cost in costs:
        if find_parent(parent, v1) != find_parent(parent, v2):
            union_parent(parent, v1, v2)
            
            answer += cost
        else:
            pass
        
    return answer
