'''
2022.11.10

【文件操作】

'''
import csv

print("董亚杰")
print()

# s = '20012332-黄心灵\n文本文件的写入方式：fp.write(s)\n文本文件的读取方式：fp.read()\n'
#
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作1.txt', 'w') as fp:
#     fp.write(s)
#
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作2.txt', 'w') as fd:
#     fd.write("辽宁省锦州市\n")
#     fd.write("渤海大学\n")
#     fd.write("软件工程专业\n")
#     fd.write("20级10班 黄心灵")
#
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作2.txt') as fp:
#     print(fp.read())
#     print(type(fp.read()))
#
# print()
#
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作2.txt') as fp:
#     for line in fp:
#         print(line)  # print()默认以换行结束
#
# print()
#
# ##读取并显示文本文件的前3个字符
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作1.txt') as fp:
#     s = fp.read(3)
#
# print(s)
#
# print()
#
# ##在PY中汉子和数字均占1个字符
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作2.txt') as fp:
#     s = fp.read(3)
#
# print(s)
#
# with open(r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作1.txt', 'a') as f1, open(
#         r'f:\大三上\大三上\Python程序设计\课堂笔记\2022.11.10文件操作2.txt', 'r') as f2:
#     f1.write(f2.read())
#
# print()
#
# '''
# cvs逗号分隔符文本格式
# import csv
# with open(csvfilepath,newline='') as f:
#     csv.reader(csvfile,dialect='excel',**fmtparams)
#     csv.reader对象和csv文件的读取
# '''
# import csv
#
#
# def readcsv1(csvfilepath):
#     with open(csvfilepath, newline='') as f:  # 打开文件
#         f_csv = csv.reader(f)  # 创建csv.reader对象
#         headers = next(f_csv)  # 标题
#         print(headers)  # 打印标题(列表)
#         for row in f_csv:  # 循环打印各行(列表)
#             print(row)
#
#
# readcsv1(r'F:\大三上\大三上\Python程序设计\课堂笔记\scores.csv')
#
# print()


def writecsv1(csvfilepath):
    headers = ['学号', '姓名', 'Python', '数据结构', '机器学习']
    rows = [('20012374', '董亚杰', '72', '85', '82'),
            ('20012488', '张三', '75', '80', '51')]
    with open(csvfilepath, 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


writecsv1(r'H:\Python程序设计-WYM\董亚杰scores.csv')









