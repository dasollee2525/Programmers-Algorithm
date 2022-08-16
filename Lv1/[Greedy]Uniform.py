def solution(n, lost, reserve):
    #lost와 reserve의 같은 번호를 각각 제거
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    #reserve의 앞 뒤 숫자가 있으면 lost와 reserve에서 삭제
    for i in real_reserve:
        if (i-1) in real_lost:
            real_lost.remove(i-1)
            continue
        elif (i+1) in real_lost:
            real_lost.remove(i+1)  
            continue
    answer = n - len(real_lost)
    return answer
