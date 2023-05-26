# H-Index

# my thoughts :
# 1. By using Sorting and Brute Force, We can solve it..!!

def solution(citations):
    citations.sort(reverse = True)
    
    for h in range(10_000, -1, -1):
        cnt = 0
        
        for citation in citations:
            if citation >= h:
                cnt += 1
            else:
                break
        
        if cnt >= h:
            return h
        else:
            continue
