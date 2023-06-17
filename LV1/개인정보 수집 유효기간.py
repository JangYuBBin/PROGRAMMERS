# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    
    today = today.split(".")
    today = int(today[0]) * 12 * 28 + int(today[1]) * 28 + int(today[2])
    # print(today)
    # 출력결과 Ex : 679551
    
    d = dict()
    
    for term in terms:
        term = term.split()
        
        d[term[0]] = int(term[1])
    # print(d)
    # 출력결과 Ex : {'A': 6, 'B': 12, 'C': 3}
    
    for i, privacy in enumerate(privacies):
        yyyymmdd, k = privacy.split()
        yyyymmdd = yyyymmdd.split(".")
        yyyymmdd = int(yyyymmdd[0]) * 12 * 28 + int(yyyymmdd[1]) * 28 + int(yyyymmdd[2])
        
        yyyymmdd += d[k] * 28
        
        if yyyymmdd <= today:
            answer.append(i + 1)
        else:
            pass
    
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
