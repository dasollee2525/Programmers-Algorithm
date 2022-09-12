from collections import deque

def solution(tickets):
    begins = []
    case = []
    for i in tickets:
        if i[0] == 'ICN':
            begins.append(i)
    
    cities = len(tickets)
    answer = []
    
    for i in begins:
        visited = [False]*(cities)
        queue = deque([(i, 0)])
        
        while queue:
            c, cnt = queue.popleft()
            answer.append(c)
            if cnt == cities + 1:
                break
            for j in range(cities):
                if tickets[j][0] == c and not visited[j]:
                    visited[j] = True
                    queue.append(ickets[j], cnt+1)
    return answer
