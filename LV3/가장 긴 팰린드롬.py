# 가장 긴 팰린드롬

# my thoughts :
# 1. By using Brute Force, We can solve it..!!
# 2. 내일 다시 풀어보도록 합시다..!!

def solution(s):
    answer = list()

    for i in range(0, len(s), 1): # <<-- "길이가 홀수인 팰린드롬 체킹..!!"
        cur_len = 1
        
        for j in range(1, len(s), 1):
            if i - j < 0 or i + j > len(s) - 1:
                break
            else:
                pass
            
            if s[i - j] == s[i + j]:
                cur_len += 2
            else:
                break
        
        answer.append(cur_len)
    
    for i in range(0, len(s), 1): # <<-- "길이가 짝수인 팰린드롬 체킹..!!"
        if i + 1 > len(s) - 1 or s[i] != s[i + 1]:
            continue
        else:
            pass
        
        cur_len = 2
        left_idx = i
        right_idx = i + 1
        
        for j in range(1, len(s), 1):
            new_left_idx = left_idx - j
            new_right_idx = right_idx + j
            
            if new_left_idx < 0 or new_right_idx > len(s) - 1:
                break
            else:
                pass
            
            if s[new_left_idx] == s[new_right_idx]:
                cur_len += 2
            else:
                break
        
        answer.append(cur_len)
    
    answer.sort(reverse = True)
    
    return answer[0]
