'''
 水仙花数即 一个三位数数字 每一位上数的立方等于该数本身
'''
print("20012374董亚杰")
#方法一：利用列表中append方法添加元素
flower=[]
for i in range(100,1000):
    a=i//100#获得百位数
    b=i//10%10#十位
    c=i%10#个位
    if a**3+b**3+c**3==i:
        flower.append(i)
print("所有的水仙花数为:"+str(flower))
#方法二：
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            a=x*100+y*10+z
            b=x**3+y**3+z**3
            if a==b:
                print("水仙花数有:"+str(a))#字符串拼接 进行强制类型转换
for i in range(100, 1000):
    a = i // 100  # 获得百位数
    b = i // 10 % 10  # 十位
    c = i % 10  # 个位
    if a ** 3 + b ** 3 + c ** 3 == i:
            print(i,end=' ')
#eval函数是将字符串转换成表达式形式输出
print("\n")
for n in range(100,1000):
    a = str(n)
    if(eval(a[0])**3+eval(a[1])**3+eval(a[2])**3==n):
           print(n,end=' ')
print("\n")
print(list(range(0,10)))
print("\n")
'''
说明：
函数map() 
格式：map(函数,序列1【，序列2，……】)
    功能： 以参数序列中的每一个元素调用函数，将调用结果写入新列表返回。
返回值：Python 2.x 返回列表、Python 3.x 返回迭代器。
例： map(lambda x: x ** 2, [1, 2, 3, 4 ])      #分析结果
'''
print(map(max,range(1,11)))
print(list(map(int,range(1,11))))
print("董亚杰")
for i in range(100,1000):#i=123
    bai,shi,ge=map(int,str(i)) #'123' '1'->1
    if bai**3+shi**3+ge**3==i:
        print(i,end=' ')
        print('\n')
'''
说明：
匿名函数：一种自定义函数
C 函数类型 函数名 形式参数  函数体
Python： 函数名 形式参数 函数体
匿名函数： 形式参数 函数体

'''
print(map(lambda x:x**2,[1,2,3,4]))
print(list(map(lambda x:x**2,[1,2,3,4])))
print('董亚杰')
# sum+map+匿名函数
for num in range(100,1000):
    if sum(map((lambda x:int(x)**3),str(num))) ==num:
        print(num,end=' ')
print()
'''
方法六：列表解析式
La=[变量赋值方法,for循环中的语句~~~]

'''
print('董亚杰')
l=[x**3+y**3+z**3 for x in range(1,10)
    for y in range(0, 10)
        for z in range(0,10)
         if (str(x)+str(y)+str(z))==str(x**3+y**3+z**3)]

print(l)


