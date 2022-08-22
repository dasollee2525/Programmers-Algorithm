def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        answer = answer + absolute if sign == True else answer - absolute
    return answer
