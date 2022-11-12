# # class Student:
# #     stuNum=0
# #     def __init__(self,sno,sname,age,gender):
# #         self.sno=sno
# #         self.sname=sname
# #         self.age=age
# #         self.__gender=gender
# #         Student.stuNum +=1
# #     def DisplayNum(self):
# #         print("当前学生总数为：",Student.stuNum)
# #     def getGender(self):
# #         return self.__gender
# #
# # s1=Student('20012374','董亚杰',20,'男')#用类创建实例化对象s1,s2
# # s2=Student('20012376','于博',20,'男')
# # # print(s1)
# # s1.DisplayNum()
# # print("学号：", s1.sno, "姓名：", s1.sname, "年龄：", s1.age, "性别：", s1.getGender())
# # s1.score=99
# # print(s1.score)
# # s2.weigh=95
# # print(s2.weigh)
#
#创建节点
class Node(object):
    def __init__(self,data):
        self.data=data    #创建一个数据域，用于存储每个结点的值
        self.next=None    #创建一个指针域，用于存储下一个结点的地址,并将其初始化为空
#创建单链表类
class SingleLinkedList:
    def __init__(self):
        self.head=Node(None) #初始化头结点函数
    #创建单链表函数
    def  CreateSingleLinkedList(self,all):
       for i in all:
           self.InsertElementInTail(i)

    #遍历单链表函数
    def TraverseElement1(self):
        cur = self.head #创建一个游标 指向头结点
        if self.IsEmpty1():
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
    def Getlength(self):
        '链表长度'
        cur = self.head.next
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    #判断单链表是否为空函数1
    def IsEmpty1(self):
        if self.head == None:
            return True
        else:
            return False

    # 判断单链表是否为空函数2
    def IsEmpty2(self):
        if self.GetLength() == 0:
            return True
        else:
            return False
    #头部插入
    def InsertElementInHead(self,node):
        node = Node(node)
        node.next = self.head
        self.head = node
    #尾部插入
    def InsertElementInTail(self,node):
        node = Node(node)
        if self.IsEmpty1():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    # 查找指定元素并返回其位置函数
    def FindElement(self, item):
        if self.IsEmpty1():
            return -1
        else:
            cur = self.head
            now = 1
            while True:
                if cur.data == item:
                    return now
                cur = cur.next
                now += 1
                if cur.next == None:
                    break
            return -1
    #删除元素函数(索引删除)
    def DeleteElement(self,item):
        if self.IsEmpty1():
            return False
        else:
            cur = self.head
            if cur.data == item:
                self.head = self.head.next
            now = 1
            while True:
                if cur.next.data == item:
                    cur.next = cur.next.next
                    return True
                cur = cur.next
                now += 1
                if cur.next == None:
                    break
        return False
    #在指定位置插入指定元素函数：检验位置合法性
    def InsElePos(self,pos,item):
        #pos为指定位置的下标
        if pos < 1:
            return False
        if pos> self.GetLength()+1:
            return False
        if pos == 1:
            self.InsertElementInHead(item)
            return True
        # 创建一个游标(指针cur),指向头结点
        cur = self.head
        #移动指针，直到找到指定位置的下标
        for i in range(1, pos - 1):
            cur = cur.next
        #创建一个保存item值的新节点
        node = Node(item)
        #把新节点node的链接域next指向插入位置的结点
        node.next = cur.next
        #将插入位置的前一个节点的链接域next指向新节点
        cur.next = node
        return True
    #在指定值后插入指定元素函数
    def InsElement2(self,pos,item):
        p=self.FindElement(pos)
        cur = self.head
        for i in range(1, p):
            cur = cur.next
        node = Node(item)
        node.next = cur.next
        cur.next = node
if __name__ == '__main__':
    lb=SingleLinkedList()
    # print(lb.IsEmpty1())
    # print(lb.IsEmpty2())
    lb.CreateSingleLinkedList([99,98,97])
    # print(lb.IsEmpty1())
    # print(lb.IsEmpty2())
    # lb.InsertElementInTail(1)
    # lb.InsertElementInTail(2)
    # lb.InsertElementInTail(3)
    lb.TraverseElement1()
    print('当前长度为',lb.Getlength())

    lb.InsertElementInHead(9)
    lb.TraverseElement1()
    print('9的位置在：',lb.FindElement(9))
    lb.DeleteElement(9)

    lb.InsElePos(2, 88)
    lb.TraverseElement1()

    lb.InsElePos(3, 77)
    lb.TraverseElement1()

    lb.InsElement2(77, 66)
    lb.TraverseElement1()

# # #创建节点
# # class Node(object):
# #     def __init__(self,elem):
# #         self.elem=elem    #创建一个数据域，用于存储每个结点的值
# #         self.next=None    #创建一个指针域，用于存储下一个结点的地址,并将其初始化为空
# # #创建单链表类
# # class SingleLinkedList:
# #     def __init__(self):
# #         self.head=Node(None) #初始化头结点函数
# #     def length(self):
# #         '链表长度'
# #         cur = self.head
# #         count=0
# #         while cur!=None:
# #             count+=1
# #             cur=cur.next
# #         return count
#
#
#
#
order = input("请输入姓名、性别并用空格隔开：")
Name = order.split(" ")[0]
Sex = order.split(" ")[1]
print(Name,Sex)