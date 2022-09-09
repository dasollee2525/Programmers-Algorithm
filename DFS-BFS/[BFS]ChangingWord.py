from collections import deque

def solution(begin, target, words):
    #keyword: 최소 몇단계의 과정
    #BFS(시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색)
    if target not in words:
        return 0

    words_num = len(words)
    word_len = len(begin)
    visited = [False]*(words_num)
    queue = deque([(begin,0)])

    answer = float('inf')
    while queue:
        w, cnt = queue.popleft()
        if w == target:
            answer = min(answer, cnt)
        for i in range(words_num):
            count = 0
            for j in range(word_len):
                if words[i][j] != w[j]:
                    count+=1
            if count == 1 and not visited[i]:
                  visited[i] = True
                  queue.append((words[i],cnt+1))              
    return answer    
#2차원 배열에서는 인덱스를 조심
