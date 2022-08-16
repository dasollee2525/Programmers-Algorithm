def solution(arr):
    answer = []
    answer.append(arr[0])
    for index in range(1, len(arr)):
        if arr[index] != arr[index-1]:
            answer.append(arr[index])
    return answer
  
  """
  def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        #a[-1]으로 슬라이싱!
        a.append(i)
    return a
    """
