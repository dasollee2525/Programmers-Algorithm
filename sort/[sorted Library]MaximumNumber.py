def solution(numbers):
    numbers = list(map(str, numbers))
    #lambda x : x * 3은 num 인자 각각의 문자열을 3번 반복
    #num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교
    numbers.sort(key=lambda x: x * 3, reverse=True)
    #모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환
    return str(int(''.join(numbers)))
