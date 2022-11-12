print(100/10)
print(10//10)
print(20%3)
#十六进制  八进制 二进制 均转换为十进制
print(0Xaf,0O35,0b1101)
#允许汉字做变量名  并可用等号 赋值
print(str("董亚杰"))
a,b,c=100,200,300
#字符串定界符 ‘’  “”  ‘’‘ ’‘’
#函数调用的嵌套  list（range（））
print("董亚杰")
for i in range(1,5):
    for j in range(6-i,1,-1):
        #输出空格，以空串结束
        print(" ",end='')
    for j in range(0,2*i-1):
        #默认以回车换行结束，end指定以空串结束
        print("*",end='')
    print("\n")

'''C语言
for(i=1;i<=10;i++){

}
1+3+5+7
 i=1,2,3,4  j=5,4,3,2


'''
