'''作业1:中国合法工作年龄为18-60岁，即如果年龄小于18的情况为童工，不合法;如果年龄在18-60岁之间为合法工龄;大于60岁为法定退休年龄。
需求:输入年龄判断输出结论
如果年龄小于18，为童工，不合法;如果年龄18-60岁之间，为合法工作年龄如果年龄大于60为退休年龄'''
print("20012374董亚杰")
age=int(input("请输入您的年龄"))
while age>0:
    if age<18 :
        print("当年年龄"+str(age)+"为合法工龄")
        break
    elif age<=60 :#不满足第一个if 执行elif
        print("当年年龄"+str(age)+"年龄不合法")
        break
    else:
        print("当年年龄"+str(age) + "年龄为退休年龄")
        break
else:
    print("请输入合法年龄")
'''作业2:坐公交:如果有钱可以上车，没有钱，不能上车;如果上车了，判断是否能坐下-—是否有空座位'''
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
else:
    print(str(money) + "车票收取失败，请再次付款，不能上车！")
'''作业3:多种方法:判断某一年是否为闰年。判断闰年的条件是:年份能被4整除但不能被100整除，或者能被400整除'''
#方法一：
year=int(input("请输入一个年份："))
if ((year%4==0)and(year%100!=0))or(year%400==0):
	print('当前年份'+str(year)+"为闰年")
else:
	print('当前年份'+str(year)+"不是闰年")
#方法二：
import calendar
year = int(input("请输入一个年份："))
check_year = calendar.isleap(year)
if check_year == True:
    print('当前年份'+str(year)+"为闰年")
else:
    print('当前年份'+str(year)+"不是闰年")
