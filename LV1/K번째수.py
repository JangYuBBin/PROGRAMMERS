# K번째수

def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        i -= 1
        j -= 1
        k -= 1
        
        temp = array[i:j + 1:1]
        temp.sort()
        
        answer.append(temp[k])
        
    return answer
