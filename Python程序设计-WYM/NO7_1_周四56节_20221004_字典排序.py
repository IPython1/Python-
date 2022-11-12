'''
复习字典



字典组成：{键1：值1，键2：值2}
访问：
    字典名[key]
    字典序列.get (key，默认值)
    字典名.keys()
    字典名. values():列表
    字典名.items():由元组构成的列表
增加：字典名[key]=值

知识点2:字典元素的添加与修改
使用字典对象的update()方法将另一个字典的键、值对添加到当前字典对象

知识点3:
使用del删除字典中指定键的元素
使用字典对象的clear()方法来删除字典中所有元素
使用字典对象的pop()方法删除并返回指定键的元素

使用字典对象的popitem(方法删除并返回字典中的一个元素

使用operator模块itemgetter方法对字典进行排序
'''
# #建立字典2
# aD = dict (name='余驭涛', age=20,id="20012277")
# print(aD)
# print(aD.keys())
# print(aD.values())
# print(aD.itetms())
#
# #创建字典方法3:使用dict利用已有数据创建字典:
# bkey = ['keya','kbyb','keyc','keyd']
# bvalue = [1,2,3,4]
# bD=dict(zip(bkey,bvalue))
# print(bD)
# print(bD. keys())
# print(bD.values)
# print(bD.items())
#
# ##创建字典方法4:以给定内容为键，创建值为空的字典
# cD = dict.fromkeys([' name', ' age', 'sex'])
# print(cD)
# print(cD.keys())
# print(cD.values())
# print(cD.items())


# aD = {'a' : 1, 'b': 2,'c': 3,'d' : 4}
# print (aD)
# aD['age'] = 18
# aD[' a'] =100
# print(aD)
# aD. update({"a":200,"aa" :666 })
# print(aD)
#
# dict1 = {'sex' : 1, 'age': 2,'word': 3,'d' : 4}
# dict2 = {'score':65}
# dict.update(dict2)
# print("更新字典dict : ", dict1)
#
# dict.update({'age’:21})
# print("更新字典dict : ",dict1)
#
# dict.update(('add':'BHU’, 'score': [ 98,97]})
# print("更新字典dict : ",dict)
# w={1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't'}
# print(w)
# #pop()删除操作  删除键值为1的键和值
# # w.pop(1)
# print(w.popitem())#删除最后一个键值对
# print(w)
import operator
from operator import itemgetter
aL = [1,2,3]
bL =[[1,2,3],[4,5,6],[7,8,9]]
# get_2=operator.itemgetter(2)
get_2=operator.itemgetter(2)
print(get_2(aL))
print(get_2 (bL))
from operator import itemgetter
# aDic = dict(a=-1,b=2,c=10,d=-2,e=10,f=2,g=-1)
# print (aDic)

from operator import itemgetter
aDic =dict(a=-1,b=2,c=10,d=-2,e=10,f=2,g=-1)
print(aDic)
print(sorted(aDic.items, key=itemgetter(0)))
# print (sorted(aDic.items))



