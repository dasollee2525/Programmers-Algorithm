def solution(price, money, count):
    result = price*(sum([i for i in range(1, count+1)])) - money
    if result <= 0:
        return 0
    else:
        return result
      
 """
#산술평균과 max의 기능을 활용해서 코드를 간결화
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
 """
