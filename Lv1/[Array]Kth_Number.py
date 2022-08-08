def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0]
        end = i[1]
        new_array = array[start-1: end]
        new_array.sort()
        index = i[2]
        result = new_array[index-1]
        answer.append(result)
    return answer

"""
#better answer
def solution(array, commands):
    answer = []
    for i, j, k in commands:
    answer.append(sorted(array[i-1:j])[k-1])
    return answer
"""
