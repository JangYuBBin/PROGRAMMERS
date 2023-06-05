# 전화번호 목록

# my thoughts :
# 1. 반복문을 활용한 Brute Force 이용시 시간초과 판정을 받을 것입니다..!!
# 2. 따라서 다른 방법을 생각해내야 합니다.
# 3. 앞 자릿수가 같아야 하므로 일단 문자열 배열(리스트)를 오름차순으로 정렬해줍니다. 자세하게 말하면 정렬 기준은 key = lambda x : x 입니다.
# 4. 정렬을 한 다음 어떤 문자열의 바로 앞 문자열이 해당 문자열의 접두어인지 확인만 해주면 됩니다..!!
# 5. 중요한 문제이므로 다음에 다시 풀어보도록 합시다..!!
# 6. 다음에 풀 때에는 어떤 문자열을 확인할 시 바로 앞 문자열이 해당 문자열의 접두어인지 확인만 해주면 되는 정당성을 함께 설명하여 풀이를 해봅시다..!!

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(1, len(phone_book), 1):
        if len(phone_book[i - 1]) <= len(phone_book[i]) and phone_book[i - 1] == phone_book[i][0:len(phone_book[i-1]):1]:
            answer = False
            return answer
        
    return answer
