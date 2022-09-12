#DFS로 문제를 접근해야 함
def solution(tickets):
    # 1. 출발지로 1차 정렬, 도착지로 2차 정렬
    tickets.sort(key=lambda x: (x[0], x[1]))
    
    # 3. 여행 루트 반환 함수. 파라미터:(남은 티켓, 현재까지의 여행 루트)
    def canTravel(tickets, route):
        # 3-2-1 성공
        if len(tickets) == 0: return route
        # 3-1
        i = 0
        while i<len(tickets) and tickets[i][0] != route[-1]: i += 1  # 지나온루트중 현위치가 tickets에 몇번째있나
        # 3-2-2 실패
        if i == len(tickets): return []  # 현재 위치가 티켓에 없다면 이 루트는 실패한 루트
        
        # 3-2
        while tickets[i][0] == route[-1]:  # 티켓의 출발지가 현재 공항이랑 같으면
            res = canTravel(tickets[:i] + tickets[i + 1:], route + [tickets[i][1]])
            # 결과 확인
            if res != []: return res  # 실패한 루트면 3-2-2에서 []를 반환 => 다음티켓을 탐색
            i += 1
        return res
    
    # 2.
    route = ['ICN']  # 현재까지의 여행루트. 처음은 ICN
    res = canTravel(tickets, route)
    
    return res
------------------------------------------------------------------------------------------------------------------------------------------------------

#BFS로 해결하려고 했으나 문제 발생 - 다음에 다시
from collections import deque

def solution(tickets):
    begins = []
    case = []
    for i in tickets:
        if i[0] == 'ICN':
            begins.append(i)
    
    cities = len(tickets)
    answer = []
    answers = []
    
    for i in begins:
        visited = [False]*(cities)
        queue = deque([(i, 0)])
        _tickets = tickets
        _tickets.remove(i)
        
        while queue:
            c, cnt = queue.popleft()
            answer.append(c[0])
            
            if cnt == cities-1:
                break
            for j in range(cities-1):
                if _tickets[j][0] == c[1] and not visited[j]:
                    visited[j] = True
                    queue.append((_tickets[j], cnt+1)) 
        answer.append(c[1])
        answers.append(answer)
        if len(answers) > 1:
            if(answers[0][1] > answers[1][1]):
                del answers[0]
            else:
                del answers[1]
    return answers[0]
