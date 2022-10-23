def solution(nums):
    select = len(nums)/2
    variety = len(set(nums))
    return min(select, variety)
