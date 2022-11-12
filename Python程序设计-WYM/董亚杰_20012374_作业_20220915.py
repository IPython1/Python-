'''
#课后作业:需求: 10位老师，5个办公室， 将10位老师随机分配到5个办公室
步骤:
1.准备数据
1.1 10位老师--列表.
1.2 5个办公室-列表嵌套
2. 分配老师到办公室
***随机分配"
就是把老师的名字写入到办公室列表--办公室列表追加老师名字数据
3.验证是否分配成功
打印办公室详细信息:每个办公室的人数和对应的老师名字
'''
print('董亚杰')
import random
offices = [[],[],[],[],[]]
teacher = ["A", "B", "C", "D", "E",
           "F", "G", "H", "I", "J" ]
random.shuffle(teacher)#人随机
for name in teacher:
    index = random.randint(0, 4)  # 生成随机整型数0-4 均为闭区间
    offices[index].append(name)  # 将老师随机的放入办公室
# print(offices)
i = 1
for office in offices:
    print("第"+str(i)+"个办公室的人数是" +str(len(office))+"人")
    i = i + 1
    for name in office:
        print("该办公室所在教师姓名为"+str(name),end=' ')
    print()
    print('----------------')