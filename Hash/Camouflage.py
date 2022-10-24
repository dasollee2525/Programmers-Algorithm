def solution(clothes):
    result = {}
    answer = 1
    for name, type in clothes:
        if type in result.keys():
            result[type].append(name)
        else:
            result[type] = [name]
    for i in range(len(result)):
        answer = answer * (len(list(result.items())[i][1])+1)
    return answer - 1
  
  #모범답안
  def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2 #굳이 딕셔너리를 새로 만들필요 없이 바로 계산을 위한 값을 넣기!!!!!!!!!!!
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
