#해당문제 모범답안
def solution(n, computers):

    visited = []    # 현재까지 방문한 모든 노드
    intranet = []   # 하나의 인트라넷을 파악하기 위한 재사용되는 리스트
    network = []    # 인트라넷으로 구성된 전체 네트워크 집합

    def connect(node):
            visited.append(node)                # 노드 첫 방문 하였으므로, 방문노드에 추가하여 어디를 안가봤는지 확인할 수 있도록 구분
            intranet.append(node)               # 지금 찾고 있는 인트라넷 구조에 현재 노드를 추가
            for nextnode in range(n):           # 현재노드와 다른 모든노드들의 관계 파악
                if nextnode not in visited and computers[node][nextnode]==1:    # 다른노드가 연결되어 있으나 방문하지 않았을 경우
                    connect(nextnode)                                           # 그 노드에 방문하여 또 이어진 노드들을 탐색
            return(intranet)                                            #만약 다 돌아서 더이상 갈 노드가 없다면, 현재까지 만들어진 인트라넷을 반환 → ①로 이동

    for node in range(n):                       # 전체 노드에 대해 한번씩은 체크
        if node not in visited:                 # 만약 방문하지 않았던 (= 인트라넷 구성이 한번도 되지 않았던) 곳이면 방문
            network.append(connect(node))       # connect 함수로 return된 인트라넷을 전체 네트워크 리스트에 추가---①
            intranet.clear()                    # 다음 인트라넷 파악을 위해 리스트 초기화

    return len(network)         #현재 파악하는것은 네트워크 개수 (= 파악했던 intranet 개수)이므로, network 배열의 길이를 반환
  
  
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
