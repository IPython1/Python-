print('董亚杰')
'''
seq:用来间隔多个对象，默认值为空格 

'''
# #list --列表
# aL = ['20012374','董亚杰','11班']
# print(type(aL))
# print(aL)
# #tuple --元组
# aT= ('董亚杰','C',99,' Python' , 99)
# print (type (aT))
# print (aT)
# # set--集合
# e= {'董亚杰','20012374','软工',}
# print (type(e))
# print(e)
# #dict —-字典—-键值对key : value
# f= {'name':'董亚杰','sex':'男','age':'20'}
# print(type (f))
# print(f)

##引入random模块
import random
print (random.randint (1,10))  #产生1到10 的一个整数 两端均为闭区间
# print (random.random ())   #产生一个0到1之间的随机浮点数 无参数
# print (random.uniform (1.1,5.4)) # 产生1.1到5.4之间随机浮点数
# print( random.randrange(100,200,5))#生成1个从1到100的(间隔为2)随机奇数（整数)
# print ( random.randrange(-100,100,7) ) #生成1个从0到100的(间隔为2)随机偶数（整数
#
# s=['a','b','c','d','e','f','g']
# print( random.choice(s))#从序列中随机选取一个元素
#
# print( random. choices(range (100), k=10))#生成由10个[0,100)随机整数构成的列表（有重复)
# print( random. choices(range (10), k=8))
#
# print (random. randint(1,100) for i in range(10))#分析? ??

# print(list(random.randint(1,100) for i in range(10)) )#独立循环生成 有重复
#
# print(tuple(random.randint(1,100) for i in range(10)) )


# print( random. sample(range(1,60),3) )#生成由5个[0,10)随机整数构成的列表 （无重复)
# al=[1,3,5,6,7]

# random. shuffle(al)#将序列a中的元素顺序打乱
# print(al)


