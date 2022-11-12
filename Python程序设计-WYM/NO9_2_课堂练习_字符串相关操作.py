# stuInfo = [
#     ['信院20-11', '20012374', '董亚杰', '男', 94],
#     ['信院20-04', '20012132', '于华美', '女', 90],
#     ['信院20-08', '20012248', '王佳铭', '男', 100],
#     ['信院20-06', '20012186', '艾浩枫', '男', 76],
#     ['信院20-04', '20012133', '井瑶函', '女', 96],
#     ['信院20-04', '20012141', '刘美玲', '女', 92],
#     ['信院20-05', '20012179', '阳运飚', '男', 98],
#     ['信院20-06', '20012184', '王乳宁', '女', 82],
#     ['信院20-10', '20012327', '艾佳馨', '女', 82],
#     ['信院20-11', '20012353', '宋杭弛', '男', 83],
#     ['信院20-08', '20012260', '孟祥竹', '男', 100],
#     ['信院20-08', '20012270', '高艺嘉', '女', 83],
#     ['信院20-11', '20012356', '苗旺', '男', 81],
#     ['信院20-09', '20012285', '刘福聪', '男', 60],
#     ['信院20-10', '20012325', '姜建名', '男', 89],
#     ['信院20-09', '20012282', '白益豪', '男', 78],
#     ['信院20-10', '20012330', '张小涵', '女', 87],
#     ['信院20-11', '20012351', '何嘉杰', '男', 86],
#     ['信院20-09', '20012287', '吴明鹏', '男', 92],
#     ['信院20-11', '20012375', '袁 萍', '女', 86]
# ]
#
# head = ['班级', '学号', '姓名', '性别', '成绩']
# # c=[]
# from operator import itemgetter
# print(" 成绩单".center(70,' '))
# print("".center(70,'-'))
# c=sorted(stuInfo,key=itemgetter(0,4),reverse=False)
# print(c)
# for i in range(len(head)):
#     print('%-8s'%head[i],end='\t')
# print()
# for item in c:
#     for i in range(len(item)):
#         print('%-8s'%item[i], end='\t')
#     print()
print('20012374董亚杰')
import string
# print(string.ascii_lowercase)
# aS=input('输入任意字符\n')
# if aS in string.ascii_uppercase:
#     print('大写')
# else:
#     print('大写之外')
# if aS>='A' and aS<='Z':   #不建议在Python中使用
#     print('大写')
# else:
#     print('大写之外')

# print(string.punctuation)#字符串
# print(string.digits)
#
#
# print(string.hexdigits)#八进制
# print(string.octdigits)
#
# print(string.whitespace)
# print(string.printable)
# from string import ascii_letters,digits
# chs=digits+ascii_letters
# print(chs)
#
# aL=[100]*10
#
# chs=digits*3
# print(chs,len(chs),max(chs))

'''
find
rfind

index
rindex

count
'''
aS='20012374,董亚杰,C,90,Java,85,PY,90'#下标0-30
# print(aS,len(aS))
# print(aS.find('90'))
# print(aS.rfind('90'))
# print(aS.rfind('900'))  #-1
#
# print(aS.index('90'))
# print(aS.rindex('90'))
# print(aS.rindex('900'))

print(aS.count('90'))
print(aS.count('900'))
'''
split指定字符分割
形成一个列表
rsplit 允许指定最大分割次数
partition 
rpartition 分为三部分
分隔符前的字符串 分隔字符串 分隔符后的字符串
'''
# print(aS.split(),2)
# print(aS.split(',',2))
# print(aS.rsplit(',',2))
print(aS.partition(','))
print(aS.rpartition('，'))#中文逗号

print(aS.rpartition('+'))#分隔符不存在 原 空 空

