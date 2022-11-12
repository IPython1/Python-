# ##张泽鑫-
# # import random
# # def generatecode (code_len = 6):
# #     char = '0123456789azwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJIKOLP'
# #     index =len(char) - 1
# #     code=''
# #     for i in range(code_len) : #[0, 6)[0,5]
# #         a = random. randint(0, index)
# #         code+=char[a]
# #     return code
# # print(generatecode())
# # char='0123456'
# # print(len(char))
# #方法三
# # import random
# # import cx_Oracleprint
# # connEcx_Oracle.connect( 'system ' o.'9rcl1521','127.0.0.1:1521/onc ')
# # def get key():
# #     key_list = []#定X宝烈表
# #     for i in range(48,58):#1-9
# #     key_list.append(chr(i))
# #     for i in range(65,91):#A-Z
# #     key_list.append(chr(i))
# #     for i in range(97,123):# a-z
# #     key_list.append(chr(i))
# #     key = random.sample(key_list,6)l
# #     #用于越取列表的指定长底的随机数:返回的是列表
# #     key_num = ''.join(key)#凝列表里的元素以太定的字符连接生成..个新的字符贵
# #     return key_num
# # randomkey三get key0.
# # print("验证码为",randomkey)共数据库存数摄刘分
# # cursor = conn.cursor(
# # sql = "insert into key values C's2 ""%(randomkey)"
# # sql2 = "select * from key"
# # cursor.execute(sql)
# # print("存储成功")
# # conn.commit
# # c=cursor.execute(sql2)
# # print(c.fetchmany(o)print("查询成功"")
# # cursor.close(conn.close(2
# '''
# append():在列表结尾追加元素或序列
# extend():在列表结尾追加数据
# 当追加序列为序列时，将序列中每个每个元素进行追加。
# insert():在指定位置新增数据 无解包功能
# '''
# aL=['20012374','董亚杰','河南省义马市']
# print(aL[2])
# # print(aL.index(20))
# # print(aL. count(20))
#
# print(len (aL))
#
# for i in aL:
#     print(i, end='，' )
# aL. append("软件工程")
# #print ()
# ##
# # aL.append(["课程1" , 80,"课程2", 88]
# # print(*aL, len(aL))
# # ##
# # ##aL.extend(["课程3”, 90,”课程4", 99])
# # ##print (*aL, len (aL) )
# # ##aL.insert(4, 100)
# # ##print (*aL, len (aL))
#
#
# aL. insert(4, ["课程5", 90,"课程6", 99])
# print (*aL, len (aL))
# ##del aL
# ##de1 aL[2]
# #aL. pop()_
# aL.pop(4)#按下标进行删除
# print (*aL,":", len (aL))
#
#
# # aL. remove(20)
# #20:值
# print (*aL,":" , len(aL))

print('董亚杰')
bL =[10,20,11,20,12,20,20,20,30]
# bL.remove(20)#20:值
# print (*bL,':',len (bL))
# print(len(bL))
# print(bL[:])
# for i in bL[:]:#左闭右开
#     print(i)
def del_20(bL):
    for i in bL[:]:
        if i == 20:
                bL.remove(20)
    return bL
result=del_20(bL)
print(*result, ':', len(result))