from itertools import product

def solution(numbers, target):
    nums = [[i, -i] for i in numbers]
    results = list(map(sum, list(product(*nums))))
    return results.count(target)
  
"""
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
"""
