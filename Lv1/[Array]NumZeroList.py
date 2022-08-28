def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if not answer:
        answer = [-1]
    else:
        answer.sort()
    return answer

"""
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""
