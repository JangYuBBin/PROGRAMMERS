# 마법의 엘리베이터 

# my thoughts :
# 1. 일의 자리의 수부터 확인하면서 더할지 뺄지 결정합시다.
# 2. 만약 현재 자리의 수가 6, 7, 8, 9라면 더해줘야 합니다.
# 3. 만약 현재 자리의 수가 1, 2, 3, 4라면 빼줘야 합니다.
# 4. 만약 현재 자리의 수가 0이라면 넘어가야 합니다.
# 5. 만약 현재 자리의 수가 5라면 다음 자리의 수까지 고려하여 결정해야 합니다.
# 6. 만약 다음 자리의 수가 5이상이라면 더해주는 것이 이득입니다.
# 7. 만약 다음 자리의 수가 5미만이라면 빼주는 것이 이득입니다.
# 8. 만약 다음 더해주는 행동을 함으로써 nums[i + 1] = 10이 되는 상황이라면 nums[i + 1] = 0으로 바꿔주고 nums[i + 2] += 1 처리를 꼭 해주어야 합니다. 이 부분을 해주지 않아 애를 먹었던 것 같습니다..!!

def solution(storey):
    answer = 0
    
    nums = [0] * 9
    
    storey = str(storey)[-1::-1]
    
    for i in range(0, len(storey), 1):
        nums[i] = int(storey[i])
    
    # print(nums)
    # 출력결과 Ex : [6, 1, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(0, len(nums), 1):
        if nums[i] == 10:
            nums[i] = 0
            nums[i + 1] += 1
            continue
        elif nums[i] == 0:
            continue
        elif 1 <= nums[i] <= 4:
            answer += nums[i]
            nums[i] = 0
        elif 6 <= nums[i] <= 9:
            answer += 10 - nums[i]
            nums[i + 1] += 1
            nums[i] = 0
        elif nums[i] == 5:
            if nums[i + 1] >= 5:
                answer += 10 - nums[i]
                nums[i + 1] += 1
                nums[i] = 0
            else:
                answer += nums[i]
                nums[i] = 0
    
    return answer

print(solution(965))
