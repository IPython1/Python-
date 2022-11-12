'''
内部函数：为紫色
1.divmod
2.a11():可迭代参数iterable中的所有元素是否都为TRUE
3.any():可迭代参数iterable 中的所有元素是否都为False
4.ascii(object):返回object所对应的字符串
集合的特点：唯一无序
'''
print('董亚杰')
#10.chr (:将(0-255)整数作为参数返回字符##a=int (97)
##a=97
##print ("chr():将（0-255)整数作为参数返回字符:" , chr(a))
#45.ord(:返回单个字符的ACII码##print("ord(’ A’) : %d"%ord('A’))##print("chr (97) :%s"%chr (97))
#31.int():将字符串转换为整数
##print(" ox10所对应的16进制数为:f".format(int('0x10’, 16)))
##print("100101所对应的2进制数为:{}".format(int ('100101',2)))
##print("123所对应的8进制数为:{}".format(int('123’,8)))
#17. eval():执行一个字符串表达式，并返回表达式的值
##str =’['a\’,l’b\', l'c\’]’
#print(eval(str))

# print(exec ("""for i in range(5): print("iter time: %d"% i)"""))#作为函数字符串参数可以到5
x = 10
expr ="""
z= 30
sum =x+y+z
print (sum)
"""
def func() :
    y = 20
    exec(expr)
    exec(expr,{"x": 1, 'y':2})
    exec(expr,{'x':1, 'y' :2},{'y': 3,'z': 4})
func ()

#16.enumerate():将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在for 循环当中。#tprint(1ist(enumerate (' abcd')) )
'''seasons = [' Spring', 'Summer', 'Fal1', 'Winter’l
print("list (enumerate(seasons))-下标从0开始: ",list(enumerate(seasons)))
print("list(enumerate(seasons,start=1))--下标从1开始: ",list(enumerate(seasons，start=1)))'''
#19.filter():过滤函数
##内置函数filter()将一个单参数函数作用到一个序列上，
#返回该序列中使得该函数返回值为True的那些元素组成的filter对象.
# #如果指定函数为None，则返回序列中等价于True的元素。
def  is_odd(n) :
    return n %2== 1  #判断是否为奇数
tmplist = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
print(tmplist)
newlist = list(tmplist)
print("filter(is_odd,[1,2,3,4,5,6,7,8,9,10l):" , newlist)
'''
简化素数代码

'''
# print('分析代码:')
# iss=int (input("输入任意正整数(>2) :"))
# if len(list(filter(lambda x: x,[iss%i!=0 for i in range(2,iss)])) == iss-2:
#     print (f" {iss}是素数")
# else:
#     print(f" {iss}不是素数")
# 35. map (funct1on,1terable)∶妪回代益
##内置函数map()把一个函数func依次映射到序列或迭代器对象的每个元素上,
##并返回一个可迭代的map对象作为结果，
##map对象中每个元素是原序列中元素经过函数func处理后的结果。
'''print(list(map(str, range(5))))
def square(x) :
    return pow (x,2)
aL=[1,2,3,4]
m=list(map(square, aL))##
for i in m:
    print (i, end=",")
# print()'''
#60.zip()和*zip(:压缩和解压缩
#zip()函数用来把多个可迭代对象中的元素压缩到一起，返回一个可迭代的zip对象##其中每个元素都是包含原来的多个可迭代对象对应位置上元素的元组
a=[1,2,3]
b=[4,5,6]
c=[8,9,10,11]
zipped=zip(a, b)
print(zipped)
print (list(zipped))
print (list(zip(a, c)))
a1, a2=zip(*zip(a, b))
print (list(a1),list(a2) , sep="")
#说明:map、filter、enumerate、zip等对象不仅具有惰性求值的特点，
# #还有另外一个特点:访问过的元素不可再次访问
x =map(str,range (10))
print (list(x))

