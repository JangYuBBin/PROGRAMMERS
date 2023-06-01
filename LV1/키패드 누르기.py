# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    
    d = dict()
    d["*"] = (0, 0)
    d[0] = (1, 0)
    d["#"] = (2, 0)
    d[7] = (0, 1)
    d[8] = (1, 1)
    d[9] = (2, 1)
    d[4] = (0, 2)
    d[5] = (1, 2)
    d[6] = (2, 2)
    d[1] = (0, 3)
    d[2] = (1, 3)
    d[3] = (2, 3)
    
    cur_left = d["*"]
    cur_right = d["#"]
    
    for number in numbers:
        if number in [1, 4, 7]:
            cur_left = d[number]
            answer += "L"
        elif number in [3, 6, 9]:
            cur_right = d[number]
            answer += "R"
        else:
            distance_l = abs(d[number][0] - cur_left[0]) + abs(d[number][1] - cur_left[1])
            distance_r = abs(d[number][0] - cur_right[0]) + abs(d[number][1] - cur_right[1])
            
            if distance_l < distance_r:
                cur_left = d[number]
                answer += "L"
            elif distance_l > distance_r:
                cur_right = d[number]
                answer += "R"
            else:
                if hand == "left":
                    cur_left = d[number]
                    answer += "L"
                else:
                    cur_right = d[number]
                    answer += "R"

    return answer
