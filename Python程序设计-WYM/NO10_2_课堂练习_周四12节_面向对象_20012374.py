'''
面向对象 封装性（一个对象中封装多个方法），在完成某个需求前，确定职责，然后根据职责寻找对象
1.类 是对一群具有 相同 特征或者行为 的事物的一个统称，是抽象的。不能直接使用
    是负责创建对象的
2.对象 不同的对象之间属性可能会各不相同
    类中定义了什么 属性和方法
类名 这类事物的名字，满足大驼峰命名法

面向过程 按顺序调用 不同的函数
'''
# class Car:
#     '''
#     class 关键字定义类 类名首字母大写
#     '''
#     price=100000
#
#     '''
#     定义类属性（类变量）price：数据成员：创建类时用变量形式表示的对象属性称为数据成员
#     类的 实例对象
#     '''
#
#     def __init__(self,c):#双下划线 c形参
#         '''
#         类的构造函数
#         self参数代表将来要创建的对象本身，并且必须是方法的第一个形参
#         在创建对象时被自动调用和执行
#         :param c:
#         '''
#         self.color=c
#
# car1=Car('Red')    #实例化对象 红车car1 蓝车car2
# car2=Car('Blue')
# print(car1.color,Car.price)#访问实例属性和类属性的值：通过“对象名.成员”的方式来访问
#
# Car.price=110000  #修改类属性
# Car.name='QQ'    #动态增加类属性
# car1.color='Yellow' #修改实例属性
# print(car2.color,Car.price,Car.name,car2.price)#访问实例属性和类属性的值：通过“对象名.成员”的方式来访问
# print(car1.color,Car.price,Car.name)#访问实例属性和类属性的值：通过“对象名.成员”的方式来访问

# class Myclass(object):
#     id=20012374
#     def f(self):
#         return Myclass.id
# x=Myclass()  #定义了类之后,可以用来实例化对象
# print(x.f())    #访问方法 实例名.方法（）
# print(x.id)         #实例名.类属性名
# print(Myclass.id)       #类名.类属性名

class Course(object):
    courseNum=0
    def __init__(self,cno,cname,credit):
        self.cno=cno   #课程编码 93013338
        self.cname = cname  #课程名字Python
        self.credit = credit    #课程学分 3
        Course.courseNum+=1

a=Course(9301338,'Python',3)
print(a.cno)
print(a.cname)
print(a.credit)
print(a.courseNum)















