'''
sort()方法没有返回值

aList.sort(key=lambda x:len( str(x) )#按转换成字符串的长度排序
列表对象提供了sort()方法支持原地排序，
而内置函数sorted()返回新列表，并不对原列表进行任何修改。
sorted()方法可以对列表、元组、字典、range对象等进行排序。
列表的sort()方法和内置函数sorted()都支持key参数实现复杂排序要求。

shuffle() 将所有元素随机排列
'''
# import random
# aL=list(range(1,11))
# random.shuffle(aL)
# print(*aL,len(aL))
#
# bL=sorted(aL)
# print(bL)
#
# cL=sorted(aL,reverse=True)
# print(cL)
'''

求最大，最小，均值等


'''
# import random
# aL = list (range (1,11))
# random.shuffle(aL)
# print (*aL)
# print(max(aL), min(aL) , sum(aL) , sum(aL)//len(aL) , sum(aL)/len(aL))

'''
元组里的元素  不可变意味着  列表中的append等操作方法在元组中无法使用
这些元素是不能修改的数据
定义元组 使用小括号且逗号隔开各个数据 数据可以是不同的数据类型
但是如果元组里面有列表，修改列表里面的数据则是支持的，故自觉很重要。
'''
# aT=(10,)
# print(type(aT))

# aT=(10,20,30,[40,10],40,10,10)
# print(type(aT))
# print(aT.index(10))#默认从下标为0开始查找10的下标
# print(aT.index(10,3))#从下标为3开始查找10的下标 ：4
# print(aT.count(10))
# # aT.append(100)
# # print(aT,len(aT))
#
# aT[3][0]=200
# aT[3].append(88)
# print(aT,len(aT))
'''
使用生成器对象_next_（）方法或内置函数next()进行遍历
创造生成器对象，

'''
# gT =((i+2)**2 for i in range (10))  #（4,9,16,）
#
# print('1',gT)
# print(tuple(gT))

# gT =((i+2)**2 for i in range (10))
#
# print('2',gT)
# print(next(gT))
# print(list(gT))#惰性  使用一次即消失
'''
字典：
答:字典，字典里面的数据是以键值对形式出现，字典数据和数据顺序没有关系，
即字典不支持下标,后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。
字典特点:
符号为大括号
数据为键值对形式出现
各个键值对之间用逗号隔开

'''
aD={'name':'董亚杰',
'age':11,
'sex':'男',
'loc':'河南省义马市'
        }
# #输出 按键输出对应值
# print(aD['name'])
#
# #按键增加对应值
# aD['Python'] = 99
# print(aD)

# 删除
# del aD['age']
# print(aD)
# aD.clear()
# print(aD)

#查找  按key值查找
'''
get()
keys()
values()
items()获取字典中的键值对  以元组的方式显示

'''
# print(aD.get('name'))
# print(aD.get('data','20220925'))
# print(aD)
# print(aD.keys())
# print(aD.values())
# print(aD.items())
'''



'''
















