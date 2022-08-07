def removeChar(n):
    if (n.isalnum() == True):
      return n
    elif (n == '-'):
      return n
    elif (n == '_'):
      return n 
    elif (n == '.'):
      return n
    else:
      return ''

def solution(new_id):
    ans = new_id.lower()
    
    ans = ''.join(list(map(removeChar, list(ans))))

    while(ans.find('..') != -1):
        ans = ans.replace('..', '.')

    ans = ans.strip('.')

    if ans == '':
      ans = 'a'

    if len(ans) >= 16:
      ans = ans[:15].strip('.')
      
    if len(ans) <= 2:
      while(len(ans) < 3):
        ans = ans + ans[-1]

    return ans  
