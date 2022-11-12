print('董亚杰')
'''1.面向对象作业
NO11-2:面向对象作业
作业1:链表应用-选择适当的数据结构实现实现页码目录翻页:
(1)初始页码为第1页
(2)当用户输入P时页码向前（由大到小）翻页
(3)当用户输入N时页码向后(由小到大）翻页
(4)每翻一页均显示当前用户所在页码
(5)若当前页为第一页，当用户输入P时无法再向前翻页并给出相应提示
(6)若当前页为最后一页，当用户输入N时无法再向后翻页并给出相应提示
(7)用户输入Q时退出程序
'''
class DLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
#Double_Link_List
class DLL():
    def __init__(self):
        self.head = DLNode(None)
    def is_empty(self):
        return self.head==None
    def CreateDLL(self,list):
        cNode = self.head
        for i in list:
            node = DLNode(i)
            cNode.next = node
            node.prev = cNode
            cNode = cNode.next
    def TraverseElement1(self):
        current_Node = self.head #创建一个游标 指向头结点
        if self.is_empty():
            print("目前链表没有数据！")
        else:
            # 创建一个游标(指针cur),指向头结点
            cur = self.head
            while True:
                print(cur.data, end=" ")
                cur = cur.next
                if cur == None:
                    break
            print()
    def PageChanging(self):
        cNode = self.head.next
        print("当前所在页码为第",cNode.data,"页，不能向前翻页了！")
        order = input("请输入操作（其中N代表向后翻页，P代表向前翻页，Q代表退出程序）：")
        while(order!= 'Q'):
            if order== 'N':
                if cNode.next == None:
                    print("当前已经是最后一页啦，无法继续向后翻页了！")
                else :
                    cNode = cNode.next
                    print("当前所在页码为：",cNode.data)
            elif order== 'P':
                if cNode.prev == self.head:
                    print("当前页数无法向前翻页，请输入合法数据")
                else :
                    cNode = cNode.prev
                    print("当前所在页码为：",cNode.data)
            else:
                print("请输入合法数据")
            order = input("请输入操作（其中N代表向后翻页，P代表向前翻页，Q代表退出程序）：")
a = DLL()
a.CreateDLL([1,2,3,4,5,6,7])
a.TraverseElement1()
a.PageChanging()
'''
作业2:链表应用-选择适当的数据结构实现学生 按性别 分两队
某校举办运动会，8名艺术班的同学被选中参加开幕式徒步方阵的表演输入参与同学的具体信息如下表所示。
序号  姓名    性别
1    蔡小天   男
2    惠娣     女
3    张玄     女
4    黄凰     女
5    侯宇     男
6   杨晓宙     男
7   李小洪     女
8   刘荒       男
在排练过程中，老师首先要求8位同学  按任意顺序  排成一队，入场时按以下规则组队并进行队形变换:
男生小分队向左，女生小分队向右，然后两队并排走入运动场。
请结合单链表中的有关操作，输出队形变换后，两支小分队中的总人数和每一位同学的姓名。
分队形后结果如下所示
男生小分队包含4个人，分别是:
蔡小天->侯宇->杨晓宙->刘荒
女生小分队包含4个人，分别是:
惠娣->张玄→>黄凰->李小洪
'''
# class StudentNode(object):
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#         self.next = None
# class SLL(object):
#     def __init__(self):
#         self.head = StudentNode(None,None)# 创建单链表头部
#     # 创建单链表函数
#     def CreateStudentListSLL(self):
#         print("请输入数据按回车确认，若想结束请输入‘#’")
#         cNode = self.head
#         order = input("请输入姓名、性别并用空格隔开：")
#         while order != "#":
#             Name = order.split(" ")[0]
#             Sex = order.split(" ")[1]
#             nNode = StudentNode(Name, Sex)
#             cNode.next = nNode
#             cNode = cNode.next
#             order = input("请输入姓名、性别并用空格隔开：")
#         # 判断单链表是否为空函数1
#     def IsEmpty1(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#     # 长度
#     def GetLength(self):
#         count = 0
#         if self.IsEmpty1():
#             return count
#         else:
#             cur = self.head
#             while True:
#                 count += 1
#                 cur = cur.next
#                 if cur == None:
#                     break
#         return count
#     # 拆分单链表函数
#     def DivideSLL(self, LLB, LLC):
#         aNode = self.head
#         bNode = LLB.head
#         cNode = LLC.head
#         while aNode.next != None:
#             aNode = aNode.next
#             pNode = aNode
#             if pNode.sex == '男':
#                 bNode.next = pNode
#                 bNode = bNode.next
#             else:
#                 cNode.next = pNode
#                 cNode = cNode.next
#         bNode.next = None
#         cNode.next = None
#     # 遍历单链表函数
#     def TraverseSLL(self):
#         cNode = self.head.next
#         while cNode.next != None:
#             print(cNode.name, "->", end="")
#             cNode = cNode.next
#         print(cNode.name)
#     # 打印函数
#     def PrintSLL(self):
#         cNode = self.head.next
#         if cNode.sex == '男':
#             print("男生小分队包含", self.GetLength(), "个人，分别是：")
#             self.TraverseSLL()
#         else:
#             print("女生小分队包含", self.GetLength(), "个人，分别是：")
#             self.TraverseSLL()
#
# if __name__ == '__main__':
#     LA = SLL()
#     LB = SLL()
#     LC = SLL()
#     LA.CreateStudentListSLL()
#     LA.DivideSLL(LB, LC)
#     LB.PrintSLL()
#     LC.PrintSLL()


