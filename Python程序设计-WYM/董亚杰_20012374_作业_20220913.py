'''
课后作业:
#编写程序，实现生成随机六位验证码的功能。
#验证码是随机生成的、包含多个天写学符、小写字母或数字的随机字符序列。#
#分析:验证码共六位，需生成六个随机字符;
.#每次生成的随机字符需存储到某数据结构之中:数据结构应具有可变、有序的特点。'''
#方法一：
# import random
# def get_code():
#     code_list = []
#     for i in range(10):   # 0~9
#         code_list.append(str(i))
#     for i in range(65, 91):  # A-Z
#         code_list.append(chr(i))
#     for i in range(97, 123):  # a-z
#         code_list.append(chr(i))
#     code = random.sample(code_list,6)   #随机取6位数
#     code_num = ''.join(code)
#     return code_num
#
# def main():
#     a = get_code()
#     print(a)
#     try:
#         x = input('请输入验证码：')
#     except ValueError:
#         print('请输入合法字符')
#     if str(x) == str(a):
#         print('Success!')
#     else:
#         print('请输入正确的验证码！')
# if __name__ == "__main__":
#         main()

# 方法二：从数据库中随机获取6位数验证码：
# connect_db：连接数据库，并操作数据库

# import pymysql
# class OperationMysql:
#     """
#     数据库SQL相关操作
#     import pymysql
# # 打开数据库连接
# db = pymysql.connect("localhost","testuser","test123","TESTDB" )
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#     """
#     def __init__(self):
#         # 创建一个连接数据库的对象
#         self.conn = pymysql.connect(
#             host='127.0.0.1',  # 连接的数据库服务器主机名
#             port=3306,  # 数据库端口号
#             user='root',  # 数据库登录用户名
#             passwd='00000000',
#             db='verify',  # 数据库名称
#             charset='utf8',  # 连接编码
#             # cursorclass=pymysql.cursors.DictCursor
# #在默认情况下cursor方法返回的是BaseCursor类型对象，BaseCursor类型对象在执行查询后每条记录的结果以列表(list)表示。
# # 如果要返回字典(dict)表示的记录，就要设置cursor参数为pymysql.cursors.DictCursor类。
#         )
#         # 使用cursor()方法创建一个游标对象，用于操作数据库
#         self.cur = self.conn.cursor()
#         print('连接成功！')
#
#     # 查询一条数据
#     def search_one(self, sql):
#         self.cur.execute(sql)
#         result = self.cur.fetchone()  # 使用 fetchone()方法获取单条数据.只显示一行结果
#         # result = self.cur.fetchall()  # 显示所有结果
#         return result
#
#     # # 更新SQL
#     # def updata_one(self, sql):
#     #     try:
#     #         self.cur.execute(sql)  # 执行sql
#     #         self.conn.commit()  # 增删改操作完数据库后，需要执行提交操作
#     #     except:
#     #         # 发生错误时回滚
#     #         self.conn.rollback()
#     #     self.conn.close()  # 记得关闭数据库连接
#
# # 插入SQL
#     def insert_one(self, sql):
#         try:
#             self.cur.execute(sql)  # 执行sql
#             self.conn.commit()  # 增删改操作完数据库后，需要执行提交操作
#         except:
#             # 发生错误时回滚
#             self.conn.rollback()
#         self.conn.close()
# #
# #     # 删除sql
# #     def delete_one(self, sql):
# #         try:
# #             self.cur.execute(sql)  # 执行sql
# #             self.conn.commit()  # 增删改操作完数据库后，需要执行提交操作
# #         except:
# #             # 发生错误时回滚
# #             self.conn.rollback()
# #         self.conn.close()
# #
# #
# if __name__ == '__main__':
#     op = OperationMysql()#通过类创建实例对象
#     res=op.insert_one("insert into user")
#     result = op.search_one("SELECT *  from verity WHERE id= ?")
#     print(result)
#方法三：
# import random,string
# str1 = "0123456789"
# str2 = string.ascii_letters#生成全部字母
# str3 = str1+str2
# code = random.sample(str3,6)
# print(*code,sep='')
#方法四：添加退出按钮
import random
import string
import tkinter as tk
import tkinter.font as tkFont
root = tk.Tk()
code = tk.StringVar()
code.set("验证码区")
verification_codes=[]  #存放所有生成过的随机码
code_string = string. digits + string. ascii_letters
def new_code() :
    verification_code =''.join (random. choices (code_string, k=6))
    code.set (verification_code)
    code_label.configure (font= (random. choice (fonts),25),fg=random.choice (colors))
    verification_codes.append (verification_code)
def roll():
    exit()
root. title("生成验证码")
root. geometry ('370x300+500+200')#界面设置大小，位置，颜色，标题
root. minsize(360, 290)
fonts = list(tkFont.families())
colors = ['red',
'green' ,
'orange',
'aqua','blue' ,'pink','purple' ,'black','grey']
code_label = tk.Label(root, textvariable=code, font=("宋体",25, "bold"),
                        fg='black',
                        height=2,
                        width=9,
                        bg="#ffffff")
code_label.pack (pady=20)#使用pack布局
button = tk.Button(root, text="下一个",height=1, width=7, command=new_code, bg="#fae2af")
button1 = tk.Button(root, text="退出",height=1, width=7, command=roll, bg="#fae2af")
button.pack()
button1.pack()
root.mainloop()
print("保存的验证码:",*verification_codes)