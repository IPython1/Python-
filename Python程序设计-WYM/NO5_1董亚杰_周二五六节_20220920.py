# def distribute_office():#随机分配
#     for i in range(5):
#         office[i][1].clear()#清空上一次分配的结社for t in teacher :
#         office[random.randint(0,4)][1].append(t)#随机地追加到某一个办公室列表中for i in range(5):
#         teacher_string[i].set( "\n\n".join(office[i][1]))#将分配的结果设置到对应的老师字符串中
#生成1-20以内的奇数列表
import random
print('董亚杰')
aL=[]
for i  in range(1,21):
    if i %2 !=0:
        aL.append(i)
# random.shuffle(aL)
print(aL,len(aL))

# b=aL.sort(reverse=True)

# print(b)
# print(aL[::])
# print(aL[::-1])#切片实现逆序输出  形成一个新列表  原来的列表不改变
# print(aL[::2])
# aaL=aL[1::2]
# print(aaL)
# print(aaL,aL)
# print(aL[3:6])
# print(aL[:100])
# print(aL[100:])
#增加
# aL[len(aL):]=[999]
# print(aL,len(aL))
# #追加列表 中间任意位置增加元素
# aL[5:5]=[555,500]
# print(aL,len(aL))
#
# aL[:0]=[100,1000]
# print(aL,len(aL))
# #修改
# aL[:3]=[100,300,500]
# print(aL[::3])
# print(aL[::2])
aL[::2]=[0]*5
print([0]*5)
print(aL,len(aL))
#删除
# aL[:3]=[]
# print(aL,len (aL))










