def changeWord(word):
    convert = ''
    for i in range(len(word)):
        if (i % 2 == 0):
            convert = convert + word[i].upper()
        else:
            convert = convert + word[i].lower()
    return convert

def solution(s):
    words = s.split()
    word_list = list(s)
    answer = ''
    temp = ''
    index = 0
    for i in words:
        temp = temp + changeWord(i)
      
    for i in word_list:
      if(i == ' '):
        answer = answer + ' '
      else:
        answer = answer + temp[index]
        index = index + 1
        
    return answer
    
"""
better way
def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
"""
