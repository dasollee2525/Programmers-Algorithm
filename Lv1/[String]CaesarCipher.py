def solution(s, n):
    z_value = ord("z") #122
    Z_value = ord("Z") #90
    lst = list(s)
    answer = []
    for c in lst:
        if c.isupper():
            next = ord(c) + n
            result = ord("A") - 1 + (next - Z_value) if next > Z_value else next
            result = chr(result)
        elif c.islower():
            next = ord(c) + n
            result = ord("a") - 1 + (next - z_value) if next > z_value else next
            result = chr(result)
        else:
            result = ' '
        answer.append(result)
    encrypt = ''.join(answer)
    return encrypt
    
"""
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
"""
"""
def caesar(s, n):
    s = list(s)
    for c in s:
        if c.isupper():
            c = chr((ord(c)-ord('A')+n)%26+ord('A'))
        if c.islower():
            c = chr((ord(c)-ord('a')+n)%26+ord('a'))
    return "".join(s)
"""
          
