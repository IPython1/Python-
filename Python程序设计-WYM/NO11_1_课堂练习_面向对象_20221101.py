print('20012374-董亚杰')
# class Book(object):
#     bookNumber=0
#     def __init__(self,bookId,bookISBN,bookName,bookPrice,bookPublish):
#         #self代表未来创建对象的本身
#         self.bookId=bookId
#         self.bookISBN=bookISBN
#         self.bookName=bookName
#         self.__bookPrice=bookPrice
#         self.__bookPublish=bookPublish
#         Book.bookNumber+=1
#
#     def ListBook(self):
#         print('编号:',self.bookId)
#         print('ISBN:',self.bookISBN)
#         print('书名:',self.bookName)
#         print('价格:',self.__bookPrice)
#         print('出版社:',self.__bookPublish)
# #类/实例.属性名
# book1=Book('1','23243535','Python',45,'清华大学出版社')
# book1.ListBook()
# print(Book.bookNumber)
# print()
from queue import LifoQueue #LIFO栈 后进先出栈
q=LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print(q.queue)
q.get()  #返回并删除尾部元素 3
print(q.queue)
q.get()
print(q.queue)
q.get()  #对空队列调用get（）方法会阻塞当前进程

from queue import Queue  #FIFO 先进先出队列
q=Queue()                 #创建对象
q.put(0)
q.put(1)
q.put(2)
print(q.queue)
q.get()  #返回并删除尾部元素 0
print(q.queue)
q.get()
print(q.queue)
q.get()  #对空队列调用get（）方法会阻塞当前进程

from collections import deque
q=deque(maxlen=5)  #创建双端队列
for item in [3,5,7,9,11]:
    q.append(item)
print(q)

q.append(13)  #队列满，左侧自动溢出
q.append(15)
print(q)
q.appendleft(5)   #从左侧添加元素，右侧自动溢出
print(q)
'''
顺序栈操作：Python里面实现栈
就是把list包装成一个类，
添加一些方法作为栈的基本操作
其他的数据结构在Python中也是以类似的方式实现的
顺序栈 顺序队列 顺序表  占用连续存储空间，可定义大小
链栈 链队列  单链表 双链表 循环(单/双)链表
#一个是连续存储，一个可以不连续存储

'''
# class Stack(object):
#     def __init__(self):
#         self._list=[]
#     def CreateStackByInput(self):
#         x=input('请输入入栈的元素：')
#         return self._list.append(x)
#     def PushStack(self,x):#入栈
#         self._list.append(x)
#     def PopStack(self):
#         """弹出栈顶元素"""
#         return self._list.pop()
#     def StackTraverse(self):
#         return self._list
#     def GetTopStack(self):
#         if self._list:#返回栈顶元素
#             return self._list[-1]
#         else:
#             return None
#     def IsEmptyStack(self):#判断当前栈是否为空
#         return self._list==[]
#     def  GetStackLength(self):#返回栈的长度
#         return len(self._list)
#
# if __name__ == "__main__":
#     s = Stack()
#     s.CreateStackByInput()
#     s.PushStack(4)#4入栈
#     s.PushStack(5)#5入栈
#     print(s.StackTraverse()) #输出此时栈中所有元素
#     print(s.GetStackLength())#输出此时栈的长度
#     print(s.PopStack())#弹出栈顶元素5 并输出
#     print(s.PopStack())#弹出栈顶元素4 并输出
#     print(s.IsEmptyStack())#验证栈是否为空 返回类型为布尔型
'''
链式存储
1.不连续2.随机分配存储空间
顺序存储
1.连续2.
'''
# class SequenceStack():
#     def _init__(self):##步骤1-2:定义构造方法__init__()
#         self.MaxStackSize=3#定义实例属性:设置顺序栈能存位
#         self.s=[None for x in range(0, self.MaxStackSize)]
#         self.top=-1#定义实例属性:设置栈顶指针top的初值为-1 表示栈为空
#
#     def CreateStackByInput(self):
#         # 排步骤1-3:定义普通实例方法:Crea
#         data = input("请输入元素(继续输入请按回车，结束输入请按“#”: ")
#         while data !='#':
#             if self.top < self.MaxStackSize - 1:
#                 self.PushStack(data)
#                 data = input("请输入元素，结束输入请按“#”:")
#             else:
#                 print("栈满")
#                 break

    # 元素出栈的函数
    ######社###################def PopStack (self) :

    # if self.IsEmptyStack():  # 判断栈是否为空，若栈空则无法执行出栈操作，给出栈if self.top==-1 :
    #     print("该顺序栈为空")
    #     return
    # else:
    #     iTop = self.top  # 栈不为空，将当前栈顶指针的值存入iTop
    #     self.top = self.top - 1  # t栈顶指针top的值减1，指向待出栈元素的下一个元素
    #     return self.s[iTop]  #返回出栈元素
    ############################

    # 获取当前栈顶元素的函数def GetTopStack(self) :##########################
'''
知识点3:init和_new方法的区别:
构造方法包括创建对象和初始化对象，在python当中，
分为两步执行:先执行new方法，然后执行__init_方法;
init是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
new_是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
new_在_init_之前被调用，_new_的返回值(实例）将传递给_init_方法的第一个参数，
然后__init_给这个实例设置一些参数。
总结
new_至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
_new_必须要有返回值，返回实例化出来的实例，这点在自己实现_new_时要特别注意，
可以retuinit_有一个参数self，就是这个_new_返回的实例，_init在new的基础上可以完成!

'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __new__(cls, name, age):
        return object.__new__(cls)
    def __str__(self,name,age):
        return 'name:{}\nage:{}\n'.format(self.name,self.age)
if __name__=='__main__':
    p=Person('DYJ',19)
    # print(p)
    print(p.__init__())



