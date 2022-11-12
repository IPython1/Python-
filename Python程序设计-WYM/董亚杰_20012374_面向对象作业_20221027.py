'''课后作业-基础
1.定义一个类：Book
2.定义类变量：bookNumber
3.定义构造函数：__init__:并且对下面成员初始化
公有成员：
bookId,bookISBN,bookName
私有成员：
__bookPrice,__bookPublish
4.给该类添加一个函数ListBook，按照如下格式显示数的信息
编号：1
ISBN：23243535
书名：Python
价格：45
出版社：清华大学出版社
定义三个对象book1,book2,boo3，
然后分别显示当前数的本数和每本书的信息
在类外分别显示每本书的价格和所在的出版社'''
class Book(object):
    bookNumber=0
    def __init__(self,bookId,bookISBN,bookName,bookPrice,bookPublish):
        #self代表未来创建对象的本身
        self.bookId=bookId
        self.bookISBN=bookISBN
        self.bookName=bookName
        self.__bookPrice=bookPrice
        self.__bookPublish=bookPublish
        Book.bookNumber+=1

    def ListBook(self):
        print('编号:',self.bookId)
        print('ISBN:',self.bookISBN)
        print('书名:',self.bookName)
        print('价格:',self.__bookPrice)
        print('出版社:',self.__bookPublish)
#类/实例.属性名
book1=Book('1','23243535','Python',45,'清华大学出版社')
book1.ListBook()
print(Book.bookNumber)
print()

book2=Book('2','10200347','C',50,'同济大学出版社')
book2.ListBook()
print(Book.bookNumber)
print()

book3=Book('3','22958652','C++',60,'浙江大学出版社')
book3.ListBook()
print(Book.bookNumber)
print()



'''
顺序栈操作：Python里面实现栈
就是把list包装成一个类，
添加一些方法作为栈的基本操作
其他的数据结构在Python中也是以类似的方式实现的
顺序栈
'''
class Stack(object):
    def __init__(self):
        self._list=[]
    def PushStack(self,x):#入栈
        self._list.append(x)
    def PopStack(self):
        """弹出栈顶元素"""
        return self._list.pop()
    def StackTraverse(self):
        return self._list
    def GetTopStack(self):
        if self._list:#返回栈顶元素
            return self._list[-1]
        else:
            return None
    def IsEmptyStack(self):#判断当前栈是否为空
        return self._list==[]
    def  GetStackLength(self):#返回栈的长度
        return len(self._list)

if __name__ == "__main__":
    s = Stack()
    s.PushStack(4)#4入栈
    s.PushStack(5)#5入栈
    print(s.StackTraverse()) #输出此时栈中所有元素
    print(s.GetStackLength())#输出此时栈的长度
    print(s.PopStack())#弹出栈顶元素5 并输出
    print(s.PopStack())#弹出栈顶元素4 并输出
    print(s.IsEmptyStack())#验证栈是否为空 返回类型为布尔型
