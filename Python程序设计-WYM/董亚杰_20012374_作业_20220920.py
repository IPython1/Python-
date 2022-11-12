'''
[作业1]．编写程序,生成一个包含20个随机整数的列表，
然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变
0 2 4 6 8 10

[作业2].生成包含20个随机数的列表，将前10个数按升序排序，
再将后10个数按降序排序后输出结果
'''
print('董亚杰')
import random

# aL=[random.randint(0,100) for i in range(20)]
# print('生成一个含20个随机整数的列表')
# print(aL,len(aL))
#
# even_numbers=aL[::2]
# print('一个含20个随机整数的列表  拿出下标偶数部分')
# print(even_numbers)
# even_numbers.sort(reverse=True)
# print('下标为偶数部分继续降序排列')
# print(even_numbers)
# print('在原列表中进行修改值形成新列表')
# aL[::2]=even_numbers
# print(aL)

#作业二
aL=[random.randint(0,100) for i in range(20)]
print('生成一个含20个随机整数的列表')
print(aL,len(aL))

print('取出前十项')
bL=aL[0:10:1]
bL.sort()  #对列表进行原地排序 默认为升序
print(bL,type(bL))

print('将列表反转取出前十项')
x=aL[::-1]
cL=x[0:10:1]
cL.sort(reverse=True)
print(cL,type(cL))
print('将列表进行合并')
result=list(bL+cL)
print(result)

