def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = b if a == 1 else sum(months[:a-1]) + b
    print(days)
    day_of_week = days % 7
    dict = {4:'MON',
            5:'TUE',
            6:'WED',
            0:'THU',
            1:'FRI',
            2:'SAT',
            3:'SUN'}
    return dict[day_of_week]
  
  """
  굳이 dict으로 하지 않고, 요일도 list로 만들어서 인덱스로 접근 가능
  def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
 """
