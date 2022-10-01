def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i, j in zip(A, B):
        answer = answer + i * j
    return answer
