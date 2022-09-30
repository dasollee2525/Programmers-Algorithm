def solution(s):
    nums = s.split()
    _nums = list(map(int, nums))
    answer = str(min(_nums)) + ' ' + str(max(_nums)) 
    return answer
