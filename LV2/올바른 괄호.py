# 올바른 괄호

# my thoughts :
# 1. By using Stack, We can solve it..!!

def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            elif stack:
                stack.pop()
    if stack:
        return False
    else:
        return True
