def solution(d, budget):
    d.sort()
    num = 0
    index = 0 
    if(sum(d) <= budget):
        return len(d)
    else:
        for i in d:
            num = num + i
            index = index + 1
            if(num > budget):
                return index - 1
            if(num == budget):
                return index
"""
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
"""
