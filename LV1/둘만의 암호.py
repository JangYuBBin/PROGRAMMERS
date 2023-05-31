# 둘만의 암호

def solution(s, skip, idx):
    answer = ''
    
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for c in skip:
        alpha.remove(c)
    
    # print(alpha)
    # 출력결과 Ex : ['a', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 's', 't', 'u', 'v', 'x', 'y', 'z']
    
    s = list(s)
    
    for i in range(0, len(s), 1):
        s[i] = alpha[(alpha.index(s[i]) + idx) % len(alpha)]
        
    answer = "".join(s)
    
    return answer
