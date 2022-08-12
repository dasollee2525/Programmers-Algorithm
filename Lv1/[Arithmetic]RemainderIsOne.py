def solution(n):
    answer = min([i for i in range(1, n) if n % i == 1])
    return answer
