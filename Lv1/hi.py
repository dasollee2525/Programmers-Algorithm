def solution(participant, completion):
    lst = list(set(participant)-set(completion))
    if not lst:
        return lst[0]
    else:
        for k, v in participant.items():
            if v >= 2: 
                return k
