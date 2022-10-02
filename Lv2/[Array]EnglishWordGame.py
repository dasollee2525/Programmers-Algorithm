def solution(n, words):
    done = []
    done.append(words[0])
    who = 0
    #for문을 통해서 순서에 맞게 가고 있는지 확인
    #이전에 나온 단어인지도 확인해야 함 -> if in
    for i in range(1, len(words)):
        if words[i] in done:
            who = i + 1
            break;
        if words[i][0] != words[i-1][-1]:
            who = i + 1
            break;
        done.append(words[i])
    if who == 0:
        return [0,0]
    else:
        if who % n == 0:
            return [n, who // n]
        else: 
            return [who % n, who // n + 1]
          
#리스트에 해당 단어가 있는지 확인하는 방법을 간소화 가능 -> words[p] in words[:p]
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
