'''
选择结构
    单分支：if 18<=age<=60:
            条件为真时执行的语句
    双分支： if：

           else：
    多分支：
        方法一：
            if：
                if：

                else：
            else：
知识点三：exit()  #kill it：关闭操作结果环境的窗口

知识点四：python容错处理
try：
    语句



except ValueError:
    exit("输出年龄有错误，请重新输入")
知识点五：
1）f:format print（f"{变量}说明文字"）
2）输出多项内容时：
    print（“董亚杰”，30，“XXX”，31，sep=“----”，end="!!!"）
3)格式化输出
    int:%d  %5d %-5d  float:%f %.2f str:%s
知识点六：fmod  divmod均为取余运算

divmod（10,-3）

import math
print(math.pi)
print(10%3,-10%3,10%-3,-10%3)
10%3=10-(10/3)*3=10-3*3=1
-10%3=-10-(-10/3)国3=-10-(-4)*3=2
-10/3=-3.333采用向向负无穷方向取最接近精确值的整数10% (-3) =10-(10/-3)*3=10-(-4)*(-3)=-2

-10%(-3） =-10-(-10/-3)*(-3)=-10-3*(-3)=-1
math.fmod (10,3)=10-(10/3)*3=10-3+3=1.0
math.fmod(-10,3)=-10-(-10/3)*3=-10-(-3)*3=-1.0
一10/3=-3.33333采用向零取整的方法计算
math.fmod (10,-3)=10-(10/-3)*(-3)=10-(-3)*(-3)=1.0
math.fmod(-10,-3)=-10-(-10/-3)*(-3)=-10-3*(-3)=-1.0
'''
print("董亚杰")
import math
print(math.pi)
print(10%3,-10%3,10%-3,-10%-3)
print(math.fmod(10,3))
# age=int(input("请输入您的年龄"))
# while age>0:
#     if age<18 :
#         print("当年年龄"+str(age)+"年龄不合法")
#         break
#     elif age<=60 :#不满足第一个if 执行elif
#         print("当年年龄"+str(age)+"为合法工龄")
#         break
#     else:
#         print("当年年龄"+str(age) + "年龄为退休年龄")
#         break
# else:
#     print("请输入合法年龄")
#     '''
#     strip()去掉空格
#     isdigit()判断是否为数字  结果为T/F
#
#     '''
# # print('abc'+'  abcdef'.strip()+'acd')
# while True :
#     age_input = input("请输入你要判断的年龄:(直接回车结束程序)").strip()
#     if age_input =='':#
#         exit("程序已结束....’")
#     if age_input.isdigit():
#         age_judge = int (age_input)
#         if age_judge >=18:
#             if age_judge > 60:
#                 print("f’{age_judge}为退休年龄!'")
#             else:
#                 print("f’{age_judge}为合法工作年龄!'")
#         else:
#             print("f’{age_judge}为童工年龄,不合法!'")
try:
    money=int(input("您当前零钱是多少呢？"+'\n'))
    while money>3:
        print(str(money)+"车票收取成功，欢迎上车！")
        empty_place = int(input("公交车空余位置为"))
        if empty_place>0:
             print("当前空余位置为"+str(empty_place) + "有空位请就坐！")
             break
        elif empty_place<=0:
            print("当前空余位置为"+str(empty_place) + "没有空位！")
            break
except ValueError:
    print("车票收取失败，请再次付款，不能上车！")
