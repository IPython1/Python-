'''

集合中数据  无序(没有下标)且唯一
可去掉重复值
元组  不可变 不可pop删除操作
'''

# aS={33,10,11,11,10,20}
# print(aS)
#
# bS=set('Hello Python')
# print(bS)
#
# cSet=set()#创建空的集合
# print(cSet)
# print(type(cSet))
#
# dSet=set(range(10,21))
# print(dSet,len(dSet))

# dSet=set([0,1,1,2,2,1,3,3,4,4,5,5,6,6,7,7,8,8,9,9])
# print(dSet,len(dSet))
#
# eSet=set([0,1,1,2,2,1,3,3,4,4,5,5])
# #增加集合中元素
# # eSet.add((1,2))   #add  以整体的方式被添加
# print(eSet,len(eSet),type(eSet))

# #update追加的数据是序列
# eSet.update([100])
# eSet.update("abc")
# print(eSet,len(eSet),type(eSet))

#删除操作
# remove()
# discard() 删除不存在的值时  不会报错

# eSet.remove(1)
# print(eSet,len(eSet),type(eSet))


# eSet.discard(10)
# e=eSet.pop()
# print(eSet)

#集合运算
a={0,1,2,3}
b={2,3,5,6,7}
c=a&b
# print(a|b)#并集运算  去掉公共元素
# print(a&b)#交集运算
# print(a^b)#对称差  并集-交集

print(a<c)#比较大小和包含关系  前边是否完全包含在后边 返回布尔值
print(c<=a)  #真子集的运算










