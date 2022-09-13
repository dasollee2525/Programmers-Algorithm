#BFS - 시작점에서 가까운 노드부터 차례대로 모든 노드를 탐색
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    #사실 line 6, 7은 필요없음..! 밑의 return 조건문으로 커버됨
    if maps[n-1][m-2] == 0 and maps[n-2][m-2] == 0 and maps[n-2][m-1] == 0:
        return -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #공간을 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #가지 못하는 공간 무시
            if maps[nx][ny] == 0:
                continue
            #처음 방문하는 경우에만 최단 거리 기록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    #이 경우를 생각하지 못해서 꽤나 해맸다..!
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]
