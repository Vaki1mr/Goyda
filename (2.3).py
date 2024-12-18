mirror = {'A':'A','H':'H','I':'I', 'M':'M', 'O' :'O', 'T': 'T', 'U' :'U', 'V': 'V', 'W': 'W', 'X' :'X', 'Y':'Y', '1' :'1' ,'8' :'8', 'E':'3', '3' :'E', 'J': 'L' , 'L':'J' , 'S':'2', '2' :'S', 'Z' : '5','5': 'Z'}
s = str(input())
flag1 = 1 # палиндром
flag2 = 1 # зеркальность
for i in range(len(s)):
    if s[i] != s[-i - 1]:
        flag1 = 0
for i in range(len(s)):
    if s[i] not in mirror:
        flag2 = 0
    else:
        if mirror[s[i]] != s[-i-1]:
            flag2 = 0
if flag1 == 0 and flag2 == 0:
    print(f'{s} is not a palindrome.')
if flag1 == 1 and flag2 == 0:
    print(f'{s} is a regular palindrome.')
if flag1 == 0 and flag2 == 1:
    print(f'{s} is a mirrored string.')
if flag1 == 1 and flag2 == 1:
    print(f'{s} is a mirrored palindrome.')