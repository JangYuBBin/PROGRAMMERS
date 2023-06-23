# 디펜스 게임 # -->> "어렵고 틀린 문제이므로 나중에 다시 풀어보아야 할 문제입니다..!!"

# another solution
# 풀이 참조 출처 : "https://velog.io/@cis07385/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%ED%8E%9C%EC%8A%A4-%EA%B2%8C%EC%9E%84"

# another thoughts :
# 1. 일단 enemy 배열을 돌면서 k를 생각하지 않고 n으로만 계속 디펜스 한다.
    # 1.1 막으면서 막은 수는 heap에 넣어준다. (최대 힙)
    # 1.2 최대 힙으로 넣는 이유는 n값이 전부 동나서 k없이 막을 수 없을 경우 지금까지 막아온 최댓값과 현재 막아야 하는 enemy의 수를 비교하기 위해서이다.
# 2. n값이 동나면 k가 남아있는지 체크해서 남아있다면 힙에 넣었던 수 중 가장 큰 수를 뽑고, 현재 막아야하는 수를 비교해 가장 큰 수를 k를 이용해서 막고, 나머지 남은 값은 n에 더해준다.
# (여기서 heap에 있는 수들은 k를 사용하지 않고 n만을 이용해서 막아낸 수들이다.)
    # 2.1 예를 들면 현재까지 7, 5, 4명을 막고 k로 막는다고 쳐보자.
    # 2.2 남은 n은 2이고, 이제 막아야할 enemy는 8명이다.
    # 2.3 그렇다면 현재까지 막아온 수 중 가장 큰 수는 7명이고, enemy는 8명이기 때문에 8명일 때 k를 이용하는게 효율적이다.
    # 2.4 heap에서 뽑았던 수 7명은 다시 heap에 넣어준다.
    # 2.5 만약 현재 막아온 수 중 가장 큰 수가 enemy보다 크거나 같다면, heap에서 뽑아낸 수를 k를 이용해서 막는게 더 효율적이다.
    # 2.6 그렇기 때문에 앞에서 그 수를 n에서 빼서 막았지만, 다시 그 수만큼 더해주고 enmey를 n을 이용해서 막아준다.
    # 2.7 그렇다면 현재 enemy[i]는 k를 이용해서 막은 것이 아니기 때문에 heap에 넣어준다. 물론 k는 깎아준다.

import heapq

def solution(n, k, enemy):
    answer = 0
    
    h = []
    
    for i, e in enumerate(enemy):
        if n >= e:
            n -= e
            heapq.heappush(h, -e)
        elif n < e:
            if k > 0:
                if h:
                    val = -heapq.heappop(h)
                    
                    if val > e:
                        n += val
                        k -= 1
                        n -= e
                        heapq.heappush(h, -e)
                    elif val == e:
                        k -= 1
                        heapq.heappush(h, -val)
                    elif val < e:
                        k -= 1
                        heapq.heappush(h, -val)
                else:
                    k -= 1
            else:
                return i
    
    return len(enemy)

print(solution(2, 4, [3, 3, 3, 3]))
