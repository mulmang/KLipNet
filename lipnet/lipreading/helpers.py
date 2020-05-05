# -*- coding: utf-8 -*- 

def text_to_labels(text):
    ret = []
    for char in text:
        if char >= u'가' and char <= u'힣':
           if char ==u'가':
               ret.append(0)
           elif char ==u'능':
               ret.append(1)
           elif char ==u'성':
               ret.append(2)
           elif char ==u'운':
               ret.append(3)
           elif char ==u'데':
               ret.append(4)
           elif char ==u'건':
               ret.append(5)
           elif char ==u'설':
               ret.append(6)
           elif char ==u'각':
               ret.append(7)
           elif char ==u'종':
               ret.append(8)
           elif char ==u'게':
               ret.append(9)
           elif char ==u'임':
               ret.append(10)
           elif char ==u'할':
               ret.append(11)
           elif char ==u'아':
               ret.append(12)
           elif char ==u'버':
               ret.append(13)
           elif char ==u'지':
               ret.append(14)
           elif char ==u'머':
               ret.append(15)
           elif char ==u'니':
               ret.append(16)
           elif char ==u'행':
               ret.append(17)
           elif char ==u'위':
               ret.append(18)
           elif char ==u'동':
               ret.append(19)
           elif char ==u'형':
               ret.append(20)
           elif char ==u'태':
               ret.append(21)
        elif char == ' ':
            ret.append(22)
    return ret

def labels_to_text(labels):
    # 26 is space, 가 = 44032 / 힣 = 55203
    text = ''
    for c in labels:
        if c >= 0 and c <= 11171:
           if c ==0:
               c=ord(u'가')
               text+=unichr(c)
           elif c ==1:
               c=ord(u'능')
               text+=unichr(c)
           elif c ==2:
               c=ord(u'성')
               text+=unichr(c)
           elif c ==3:
               c=ord(u'운')
               text+=unichr(c)
           elif c ==4:
               c=ord(u'데')
               text+=unichr(c)
           elif c ==5:
               c=ord(u'건')
               text+=unichr(c)
           elif c ==6:
               c=ord(u'설')
               text+=unichr(c)
           elif c ==7:
               c=ord(u'각')
               text+=unichr(c)
           elif c ==8:
               c=ord(u'종')
               text+=unichr(c)
           elif c ==9:
               c=ord(u'게')
               text+=unichr(c)
           elif c ==10:
               c=ord(u'임')
               text+=unichr(c)
           elif c ==11:
               c=ord(u'할')
               text+=unichr(c)
           elif c ==12:
               c=ord(u'아')
               text+=unichr(c)
           elif c ==13:
               c=ord(u'버')
               text+=unichr(c)
           elif c ==14:
               c=ord(u'지')
               text+=unichr(c)
           elif c ==15:
               c=ord(u'머')
               text+=unichr(c)
           elif c ==16:
               c=ord(u'니')
               text+=unichr(c)
           elif c ==17:
               c=ord(u'행')
               text+=unichr(c)
           elif c ==18:
               c=ord(u'위')
               text+=unichr(c)
           elif c ==19:
               c=ord(u'동')
               text+=unichr(c)
           elif c ==20:
               c=ord(u'형')
               text+=unichr(c)
           elif c ==21:
               c=ord(u'태')
               text+=unichr(c)
        elif c == 22:
            text += ' '
    return text
#def text_to_labels(text):
#    ret = []
#    for char in text:
#        if char >= 'a' and char <= 'z':
#            ret.append(ord(char) - ord('a'))
#        elif char == ' ':
#            ret.append(26)
#    return ret#

#def labels_to_text(labels):
#    # 26 is space, 27 is CTC blank char
#    text = ''
#    for c in labels:
#        if c >= 0 and c < 26:
#            text += chr(c + ord('a'))
#        elif c == 26:
#           text += ' '
#    return text
