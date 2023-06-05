# 모음사전

# my thoughts :
# 1. By using Brute Force and Sorting, We can solve it..!!

def solution(word):
    answer = 0
    
    words = set()
    
    for c1 in ["", "A", "E", "I", "O", "U"]:
        for c2 in ["", "A", "E", "I", "O", "U"]:
            for c3 in ["", "A", "E", "I", "O", "U"]:
                for c4 in ["", "A", "E", "I", "O", "U"]:
                    for c5 in ["", "A", "E", "I", "O", "U"]:
                        temp = c1 + c2 + c3 + c4 + c5
                        if not temp:
                            continue
                        else:
                            words.add(temp)
    
    words = list(words)
    words.sort() # <<-- "사전 순 정렬..!!"
    
    answer = words.index(word) + 1
    
    return answer

print(solution("AAAAE"))
