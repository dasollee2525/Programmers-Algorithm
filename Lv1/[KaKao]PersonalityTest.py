def max(dict, key_a, key_b):
    if dict[key_a] > dict[key_b]:
        return key_a
    elif dict[key_a] < dict[key_b]:
        return key_b
    else:
        return key_b if key_b < key_a else key_a

def solution(survey, choices):
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for type, score in zip(survey, choices):
        if score > 4:
            dict[type[1]] += abs(score-4)
        elif score < 4:
            dict[type[0]] += abs(score-4)
    print(dict)
    answer = max(dict, 'R', 'T') + max(dict, 'C', 'F') + max(dict, 'J', 'M') + max(dict, 'A', 'N') 
    return answer
