# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    for i in range(0, len(s), 1):
        if i == 0: # <<-- "단 인덱스가 0일 때는 주의합시다."
            answer += s[i].upper()
        elif s[i - 1] == " " and s[i].isalpha(): # <<-- "즉, 단어의 첫 문자일 때는 대문자로 바꿔줍니다."
            answer += s[i].upper()
        else: # <<-- "그 외의 경우에는 소문자로 씁니다."
            answer += s[i].lower()
    return answer
