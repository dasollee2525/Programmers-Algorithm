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

"""
advanced_answer

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
 """
