def solution(progresses, speeds):
    tasks = [(100-p)//s if (100-p)%s > 0 else (100-p)//s+1 for p, s in zip(progresses, speeds)]
    answer = []
    while tasks:
        count = 0
        tasks = [i-tasks[0] for i in tasks]
        print(tasks)
        tasks.pop(0)
        count = count + 1
        if tasks:
            break
        while tasks[0] <= 0:
            tasks.pop(0)
            count = count + 1
        answer.append(count)
    return answer
