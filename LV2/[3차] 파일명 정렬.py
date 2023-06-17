# [3차] 파일명 정렬

# my thoughts :
# 1. 문제의 조건에 맞게 HEAD, NUMBER, TAIL 3부분으로 나눈다.
# 2. 그런다음 문제의 조건에 맞게 정렬 기준을 세운 후 정렬 후 정답을 출력한다..!!

def solution(files):
    answer = []
    
    arr = list()
    
    for idx, file in enumerate(files):
        head_start = 0
        head_end = 0
        
        for i in range(0, len(file), 1):
            if file[i].isalpha() or file[i] in [" ", ".", "-"]:
                head_end = i
            else:
                break
        
        number_start = head_end + 1
        number_end = head_end + 1

        for i in range(number_start, len(file), 1):
            if file[i].isdigit():
                number_end = i
            else:
                break
        
        arr.append((file[head_start:head_end + 1:1].lower(), int(file[number_start:number_end + 1:1]), idx, file))
    
    # print(arr)
    # 출력결과 Ex : ....
    
    arr.sort(key = lambda x : (x[0], x[1], x[2]))

    for HEAD, NUMBER, idx, origin in arr:
        answer.append(origin)
        
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
