#stack을 활용하는 문제
#stack을 온전하게 활용하려면 append부터 시작해야 한다.
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack == []:
                return False
            else:
                stack.pop() #굳이 ")"을 신경써줄 필요가 없다는 것이 포인트
    return stack==[]
