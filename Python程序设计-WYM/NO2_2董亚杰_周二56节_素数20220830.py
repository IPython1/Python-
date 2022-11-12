'''
第二周 周二56节 20220830
知识点1：变量  = input("说明文字：参数为字符串")
            类型转换函数 int（）  float（） eval（）
知识点2：for-else  while-else

'''
import math
print("董亚杰")
'''
素数  除了1和它本身没有其他的因数

'''

#方法一
'''sr=int(input('请输入一个数'))
js=0
for jy in range(1,sr):
    if sr%jy==0:
        js+=1
if js==1:
    print("输入的数为素数")
else:
    print("输入的数不为素数")
print()''' #end  默认回车
#方法二：循环正常结束之后执行第二个else
# zs = int(input("请输入一个整数："))
# if zs<2:
#   print(str(zs)+"这个数不是素数")
# else:
#  #for i in range(2，zs//2+1):
#  # for i in range(2，int(math.sqrt(zs))+1):
#  for i in range(2,zs):
#     if zs%i==0:
#         print(str(zs)+"这个数不是素数")
#         break
#     else:
#         None
#  else:
#      print(str(zs)+'这个数是素数')
# print("over!")
#方法三：
'''n=int(input("请输入一个正整数n："))
if n<2:
  print("%d不是素数！"%n)
else:
  for i in range(2,n):
      if n%i==0:
          print("%d不是素数！"%n)
          break
  else:
       print("%d是素数！"%n)'''
'''需求1:道歉5遍"忘带口罩，我错了"，完成之后执行得到原谅我
1.书写道歉的循环
2.循环正常结束要执行的代码—-else'''
# i = 1
# while i <= 5:
#     print('忘带口罩，我错了')
#     i+=1
# else:
#     print('原谅你了！')
'''--------------------'''
# i = 10
# while i <= 5:#条件为假：循环体不执行
#     print('忘带口罩，我错了')
#     i+=1
# else:
#     print('2:高姿态的i=10>5 并未道歉，绝不原谅!@@!!(循环体并未执行执行)')
# print("over!")
'''----------------- '''
# i= 1
# while i <= 5:
#     print("远离新冠戴好口罩")
#     if i== 3:
#          break
#     i += 1
# print("’重要事情说三遍!，哈哈哈哈’")
'''-------------------'''
#方法四：
'''print ("余驭涛:")
print("素数判断程序")
sr=int (input ("’请输入一个数’"))
js=0
while sr<2:#分析:输入错误??
    print ("输入异常,请重新输入")
    sr=int(input("请输入一个数’"))
else:
    for jy in range (1, sr):
        if sr%jy==0:
            js+=1
    if js==1:
        print ("输入的数为素数")
    else:
        print("输入的数不为素数")
print("'\n’")'''
#方法五：
import os
print("孙可欣","is prime or not")
while 1:
    iss=int(input("type a number:"))
    if len(list(filter(lambda x:x,[iss%i!=0 for i in range(2,iss)]))) == iss-2:
        print("This number is prime! QWQ")
    else:
        print("This number is not prime! TAT")
    depth = 'python 孙可欣0826.py'
    os.system(depth)
#print([iss%i!=0 for i in range(2,iss)])#列表表达式
''' filter 将数列中每个元素作为参数'''
#方法六：
num =int(input("请输入一个数字:"))
emptyList = []#空列表
if num < 2:
    print (num,"不符合要求")
else:
    if emptyList == [num % k for k in range(2,int(num * 0.5) + 1) if num % k == 0]:
        print (num,"是素数")
    else:
        print (num,"不是素数")



















