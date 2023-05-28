# 시저 암호

def solution(s, n):
    answer = ''
    alpha_s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alpha_b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for c in s:
        if c.islower():
            answer += alpha_s[(alpha_s.index(c) + n) % 26]
        elif c.isupper():
            answer += alpha_b[(alpha_b.index(c) + n) % 26]
        else:
            answer += c
    
    return answer
