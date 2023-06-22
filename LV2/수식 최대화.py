# 수식 최대화

# my thoughts :
# 1. 순열 라이브러리를 활용하여 문제를 해결해봅시다..!!
# 2. 그 전에 일단 숫자와 연산자를 분리하는 작업을 해주어야 합니다.
# 3. 그다음 연산자의 우선순위로 나올 수 있는 경우를 모두 계산해줍시다..!!
# 4. ....

from itertools import permutations
from collections import deque

def solution(expression):
    answer = list()
    
    nums = list()
    ops = list()
    
    cur_num = ""
    for c in expression:
        if c.isdigit():
            cur_num += c
        else:
            nums.append(int(cur_num))
            cur_num = ""
            
            ops.append(c)
    
    nums.append(int(cur_num))
    
    # print(nums)
    # 출력결과 Ex : [100, 200, 300, 500, 20]
    # print(ops)
    # 출력결과 Ex : ['-', '*', '-', '+']
    
    cases = list(permutations(["+", "-", "*"], 3))
    
    # print(cases)
    # 출력결과 Ex : [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
    
    for case in cases:
        case = deque(case)
        
        copy_nums = nums[:]
        copy_ops = ops[:]
        
        while case:
            cur_op = case.popleft()
            
            i = 0
            while i <= len(copy_ops) - 1:
                if copy_ops[i] == cur_op:
                    if copy_ops[i] == "+":
                        copy_nums[i] = copy_nums[i] + copy_nums[i + 1]
                    elif copy_ops[i] == "-":
                        copy_nums[i] = copy_nums[i] - copy_nums[i + 1]
                    elif copy_ops[i] == "*":
                        copy_nums[i] = copy_nums[i] * copy_nums[i + 1]
                    
                    copy_nums.pop(i + 1)
                    copy_ops.pop(i)
                else:
                    i += 1
        
        answer.append(abs(copy_nums[0]))
    
    answer.sort(reverse = True)
        
    return answer[0]
