def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(n):
        hIndex = n-i
        #citations[i]가 hIndex보다 크거나 같으면, answer에 hIndex를 저장하고 반복을 멈춥니다. 
        if citations[i] >= hIndex:
            answer = hIndex
            #왜 바로 return을 하면 안되지..?
            break
    return answer
