def solution(num):
    count = 0
    if num == 1:
        return 0
    while(num != 1):
        if (num % 2 == 0):
            num = num // 2
        else:
            num = num * 3 + 1
        #num = num // 2 if num % 2 == 0 else num * 3 + 1 가능!
        count = count + 1
        if(count == 500):
            return -1
    return count
