'''作业：

提供以下3个银行账户，每个账户有3次输入密码的机会，正确执行
（1）错了，账户错了，密码错了，只有3次
（2）对了，办理取款、存款、退卡业务
card1："1001"   password1："123456"  ban1=10000
card2："1002"   password2："123456"  ban2=10000
card3："1003"   password3:"123456"   ban3=10000'''
print("董亚杰")
usrname=['1001','1002','1003']
password=['123456','123456','123456']
ban=[8810,8820,8830]
# 进入登录界面，flag0指的是输入密码错误的次数
# flag1指的是登录成功标志位
flag0 = 0
flag1 = 1
print(">>>>User Login<<<<<")
print(">>>>  用户登录中 <<<<<")
while True:
    # 提示用户输入用户名
 usr = input("请输入用户名:")
 try:
    i=usrname.index(usr)
    print(i)
    break
 except ValueError:
        flag0 += 1
        if flag0 < 3:
            print("用户名错误，请重新输入!")
        if flag0 == 3:
            print("你已经失败三次了，请重新登录")
            break

if usr == usrname[i] :
        # 输入用户名正确则进入到输入登录密码阶段
        # 判断输错登录密码次数
        # i=usrname.index(usr)
        # print(i)
        while flag0 < 3:
            password0 = input("请输入密码:")
            # i = usrname.index(usr)
            # print(i)
            if password0 == password[i]:
                # 若密码输入正确则登录成功因而跳出循环
                print("Success Login（登录成功）!")
                flag1 = 1
                try:
                    thing=int(input("请输入您当前想办理的业务：（0取款，1存款，2退卡）"))
                    if thing==0:
                        print("------取款loading-------")
                        money=int(input("请输入您当前取款数："))
                        ban[i]=ban[i]-money
                        if (ban[i])<0:
                            print("余额不足！")
                            break
                        else:
                            print("当前余额为："+str(ban[i]))
                            break
                    if thing==1:
                        print("------存款loading-------")
                        money = int(input("请输入您当前存款数："))
                        ban[i] = ban[i] +money
                        if (ban[i])<0:
                            print("余额不足！")
                            break
                        else:
                            print("当前余额为：" + str(ban[i]))
                            break
                    if thing==2:
                        print("------退卡-------")
                        usrname.remove(usrname[i])
                        break
                except ValueError:
                    print("抛出异常")

            else:
                # 计算输错次数，每输错一次flag加1
                flag0 += 1
                if flag0 < 3:
                    print("密码错误，请重新输入!")
# 输错三次跳出输入密码环节重新进行用户名的输入，相应的flag也要归零
            if flag0 == 3:
                print("你已经失败三次了...")
                break
