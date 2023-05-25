# 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]
    
    before = words[0]
    already = set()
    already.add(before)
    
    for i in range(1, len(words), 1):
        if words[i][0] == before[-1] and words[i] not in already:
            already.add(words[i])
            
            before = words[i]
        else:
            q, r = divmod(i + 1, n)
            if r == 0:
                answer[0] = n
            else:
                answer[0] = r
            
            if r == 0:
                answer[1] = q
            else:
                answer[1] = q + 1
            
            return answer
        
    return [0, 0] # <<-- "주어진 단어만으로는 탈락자가 발생하지 않으므로 [0, 0]을 리턴해주면 됩니다..!!"
