import operator
from operator import itemgetter
print('董亚杰')
# persons = [{'name':'Dong', 'age':37},
#                {'name':'Zhang', 'age':40},
#                {'name':'Li', 'age':50},
#                {'name':'Dong', 'age':43},
#                 {'name':'董亚杰', 'age':20}]
#
# print(persons)
# print(sorted(persons,key=lambda x:(x['name'],-x['age'])))#姓名字符型默认升序  按年龄相反数的升序进行排序（即降序排列）
#
# ##使用operator模块itetngetter方法对字典进行排序
# aL= [1,2,3]
# bL = [[1,2,3],[4,5,6],[7,8,9]]
# get_2=operator.itemgetter(2)  #获取列表中下标为2的元素
# print(get_2(aL))
# print(get_2(bL))
#
#
# aDic = dict (a=-1,b=2,c=10,d=-2,e=10,f=2,g=-1)
# print(aDic)
# print(sorted(aDic.items(),key=itemgetter(1)))#定义排序规则
# print(sorted(aDic.items(),key=itemgetter(0)))
#
#
# gameresult = [{'name':'Pob', 'wins':10, 'losses':3, 'rating':75.0},
#               {'name':'David', 'wins':9, 'losses':5, 'rating':57.0},
#               {'name':'Carol', 'wins':9, 'losses':5, 'rating':57.0},
#               {'name':'Batty', 'wins':10, 'losses':3, 'rating':72.8},
#               {'name':'董亚杰', 'wins':10, 'losses':3, 'rating':72.8}]
# #按'wins'升序，该值相同的按'name'升序排序
# print(sorted(gameresult,key=lambda x:(x['wins'],x['name'])))
# print(sorted(gameresult,key=itemgetter('wins','name')))

# phonebook = {'Linda':'16504167750',
#              'Bob': '15804169345',
#             'Carol':'18604165834',
#              '董亚杰': '19916335652' }
# print(sorted(phonebook,key=itemgetter(0)))
# print(sorted(phonebook,key=itemgetter(1)))
#
# gL= [
#     ['Bob',95.0,'A'],
#     ['Alan',83.5, 'C'],
#     ['Mandy',83.5, 'A'],
#     ['Bob',89.3,'E'],
#     ['Bob',89.3,'E']
#     ]
# print("按姓名升序，姓名相同按分数升序排序")
# print(sorted(gL,key=itemgetter(0,1)))
# print("按分数升序，分数相同的按姓名升序排序")
# print(sorted(gL,key=itemgetter(1,0)))
# print("按等级升序，等级相同的按姓名升序排序")
# print(sorted(gL,key=itemgetter(2,0)))

aL = ["4what", "1I'm", "3sorting", "2by","1I'm",'5董亚杰']
bL = ["something", "else", "to", "sort","able",'董亚杰']
#
#
# print(aL)
# print(bL)
# print("根据另外一个列表bL的值来对当前列表aL元素进行排序时，al与bL有重复元素时结果有误")
# print(sorted(bL,key=lambda item: aL[bL.index(item)]))
# print("根据另外一个列表aL的值来对当前列表bl元素进行排序时，将列表al与bL通过zip合并为一个列表")
# abL= zip(aL,bL)
# print(abL)
# print(type(abL))
# print()
# abLzip=sorted(abL)
# print(type(abLzip))
# print(abLzip)
# print()
# result = [x[1] for x in abLzip]
# print(result)

#字典推导式
s = {x :x.strip() for x in ('strLR ', '  strR  ','   strL  ')}
print (s)
for k,v  in s.items():
    print(k,v)
    # 1 2 3 4 5
x = ['A','B', 'C', 'D']
y=['a', 'b', 'b', 'd']
bD= {i:j for i, j in zip(x,y)}
print(bD)

import random
from random import  randrange
# random.randint(15)
stu = {'stu'+str(i+1):random.randint(1, 5) for i in range(15) if random.randint(0,1)}
score = {'stu'+str(randrange(1,16)) : randrange(1,6) for i in range(5)}
print(stu)
print(score)