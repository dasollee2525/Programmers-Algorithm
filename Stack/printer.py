def solution(priorities, location):
    queue = [(i,q) for i,q in enumerate(priorities)]
    answer = 0
    while(1):
        x = queue.pop(0)
        if any(x[1] < p[1] for p in queue):
            queue.append(x)
        else:
            answer = answer + 1
            if x[0] == location:
                return answer
