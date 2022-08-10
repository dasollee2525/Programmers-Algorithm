from itertools import combinations as cb

def solution(numbers):
    result = map(sum, list(cb(numbers, 2)))
    answer = list(set(result))
    answer.sort()
    return answer
