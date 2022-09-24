def solution(today, terms, privacies): 
  criteria = dict() 
  result = [] 
  for j in terms: 
    char, num = j.split() 
    num = int(num) 
    criteria[char] = num 
    
    #compare today-privacies' date with term 
    t_year, t_month, t_day = today.split('.') 
    for index, i in enumerate(privacies): 
      date, term = i.split() 
      year, month, day = date.split('.') 
      y = int(t_year) - int(year) 
      m = int(t_month) - int(month) 
      d = int(t_day) - int(day) 
      total = 12*28*y + 28*m + d 
      if total >= criteria[term] * 28: 
        result.append(index+1) 
  return result
