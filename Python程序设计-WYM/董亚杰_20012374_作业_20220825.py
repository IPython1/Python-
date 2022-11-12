'''
作业
作业1:输入任意整数，判断是否是素数 素数即只有1和它本身没有其他的因数
'''




print("20012374董亚杰")
#方法一：
zs = int(input("请输入一个整数："))
for i in range(2,zs):
    if zs%i==0:
        print(str(zs)+"这个数不是素数")
        break
    else:
        None
else:
     print(str(zs)+'这个数是素数')

'''
作业2:自学以下运算
#注意:先算复合赋值运算符右面的表达式;
算复合赋值运算c = 10
c += 3 -- c = c +3
#不支持--++运算
print (c)
c += 1 +2print (c)
d = 10
d *= 1 +2print (d)
a = 0b = 1c = 2
#1. and:与:都真才真
print ((a< b) and (c >b))print(a > b and c > b)
#2.or:或:一真则真,都假才假print (a < b or c >b)
print (a > b or c >b)
#3. not:非:取反print (not False)print (not c >b)
'''
c=10
c+=10
print(c)
c=10
c+=1+2
print(c)
d = 10
d *= 1 +2
print (d)
a = 0
b = 1
c = 2
#1. and:与:都真才真
print((a< b) and (c >b))
print(a > b and c > b)
#2.or:或:一真则真,都假才假
print (a < b or c >b)
print (a > b or c >b)
#3. not:非:取反
print (not False)
print (not c >b)



