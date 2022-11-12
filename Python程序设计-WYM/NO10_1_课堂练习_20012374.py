print('20012374董亚杰')
# aS='20012374,董亚杰,C,90,Java,85,PY,90'
# print(aS.split(','))
# aL=['20012374','董亚杰','C#','99','JavaWeb','88','Python','90']
# print(aL)

# #join()
# # bS=','.join(aL)
# # bS='-'.join(aL)
# # bS=''.join(aL)
# # print(bS,type(bS),len(bS))
# import random
# from string import ascii_letters,digits
# chs=digits+ascii_letters #10+52=62
#
# #三种方法 产生随机码
# # m1=''.join(random.choice(chs) for _ in range(6))
# # print(m1)
# #
# # m2=''.join(random.sample(chs,6))
# # print(m2)
# #
# # m3=''.join(random.choices(chs,k=6))
# # print(m3)
#
#
aS='r20012374 董亚杰,C 90,Java 85,pY,90'
# print(aS.lower(),aS.upper(),sep='\n')
# #capitalize 字符串首字母大写  title 每个单词的首字母大写 swapcase 大小写互换
# print(aS.capitalize(),aS.title(),aS.swapcase(),sep='\n')
#
print(aS.replace('0',''))#使用空串进行替换：删除操作
#
# #maketrans()  返回一个字典、translate
gz=''.maketrans('abc012','ABC+-*')
print(gz)
# # print(gz.keys())
# # print(gz.items())
# # for k,v in gz.items():
# #     print(k,v,end=',')
print(aS.translate(gz))
import string
#字符串加密 maketrans() translate() 方法实现了   加密算法

# def kaisa(s,k):#切片左闭右开
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#     before = string.ascii_letters
#     after=lower[k:]+lower[:k]+upper[k:]+upper[:k]
#     table = ''.maketrans(before,after)  #创建映射表
#     return s.translate(table)
# s='Python is a greate programming language. I like it!'
# print(kaisa(s,3))

import string
# sel = input('input 0-1:')
# print(len(sel))
# #strip  删除开头和结尾的空格
# if sel.strip()=='0':
#     print('sel:'+sel.strip()+'!')
#     print('sel:' +sel.lstrip()+'!')
#     print('sel:' +sel.rstrip()+'!')
#
# # sel = input('input 0-1:').strip()
# # print(len(sel))
# # if sel is '0':
# #     print('sel:',sel) #sep默认 '空格'
#
# aS='r00000020012374,董亚杰,C,90,Java 85,PY,90    000'
# print(aS.strip('0'))
# aS='r20012374 董亚杰,C 90,Java 85,pY,90'
# print(aS.startswith('0'),aS.endswith('0'))#返回 False  True
# aS='121000'
# print(aS.isalnum())
# print(aS.isalpha())
# print(aS.isdigit())
# print(aS.isspace()) #空格  \t \n
# print(aS.isupper())
# print(aS.islower())


'''
center（50，‘-’） 居中对齐
ljust() 左对齐
rjust() 右对齐
'''
# print('菜单'.center(50,' '))
# print(''.center(50,'-'))
# print('1-红烧肉'.ljust(50,' '))
# print('2-红烧肉'.rjust(50,' '))
# print('2-红烧肉'.center(50,' '))
# for i in range(6):#0 1 2 3 4 5
#     print(''.center(i,'*')) #*的个数
# print(i)



















