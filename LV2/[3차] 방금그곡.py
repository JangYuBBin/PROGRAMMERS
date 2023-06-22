# [3차] 방금그곡

# my thoughts :
# 1. (예를 들자면) C# -->> c로 변환하는 과정을 거쳐서 문자열 비교를 용이하게 해줍시다..!!

def solution(m, musicinfos):
    answer = list()
    
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    
    for i in range(0, len(musicinfos), 1):
        musicinfos[i] = musicinfos[i].split(",")
        musicinfos[i][3] = musicinfos[i][3].replace("C#", "c")
        musicinfos[i][3] = musicinfos[i][3].replace("D#", "d")
        musicinfos[i][3] = musicinfos[i][3].replace("F#", "f")
        musicinfos[i][3] = musicinfos[i][3].replace("G#", "g")
        musicinfos[i][3] = musicinfos[i][3].replace("A#", "a")
        
        musicinfos[i][0] = list(map(int, musicinfos[i][0].split(":")))
        musicinfos[i][0] = musicinfos[i][0][0] * 60 + musicinfos[i][0][1]
        
        musicinfos[i][1] = list(map(int, musicinfos[i][1].split(":")))
        musicinfos[i][1] = musicinfos[i][1][0] * 60 + musicinfos[i][1][1]
    
    # print(musicinfos)
    # 출력결과 Ex : 	[[720, 734, 'HELLO', 'CDEFGAB'], [780, 785, 'WORLD', 'ABCDEF']]
    
    for i, musicinfo in enumerate(musicinfos):
        time = musicinfo[1] - musicinfo[0]
        
        q, r = divmod(time, len(musicinfo[3]))
        
        check = musicinfo[3] * q + musicinfo[3][0:r:1]
        
        # print(check)
        # 출력결과 Ex : CDEFGABCDEFGAB
        
        if m in check:
            answer.append((musicinfo[2], time, i))
    
    if not answer:
        return "(None)"
    else:
        answer.sort(key = lambda x : (-x[1], x[2]), reverse = False)
        return answer[0][0]
