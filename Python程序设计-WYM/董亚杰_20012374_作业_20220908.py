'''
吏用序号产生幸运奖随机3人，输出姓名（第11人为本人姓名)
1.于华美
2.井瑶函
3.刘美玲
4.陈世茂
5.王慧道
6.刘书成
7.李纹竹
8.张俊锋
9.伊泓钢
10.阳运飚
11.董亚杰
'''
import random
print('董亚杰')
#方法一：返回列表
lucky_boy=random. sample(range(0,11),3)
print(lucky_boy)
boy=["于华美","井瑶函","刘美玲","陈世茂","王慧道","刘书成","李纹竹","张俊锋","伊泓钢","阳运飚","董亚杰"
]
for i in range(0,3):
    index=lucky_boy[i]
    print("幸运学生有"+str(index+1)+"号",end="-")
    print(boy[index])
#方法二：构建字典
nice_boy={
1:"于华美",
2:"井瑶函",
3:"刘美玲",
4:"陈世茂",
5:"王慧道",
6:"刘书成",
7:"李纹竹",
8:"张俊锋",
9:"伊泓钢",
10:"阳运飚",
11:"董亚杰"
}
lucky_boy=random. sample(range(1,12),3)
for i in range(0,3):
    index = lucky_boy[i]
    print('幸运学生有'+str(index)+'号'+nice_boy[index])
