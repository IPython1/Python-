'''
1-定义一个空列表dInfo,
将表头列表head和学生信息列表suInfo，分别转换为字典元素的键和值，
格式如下:学号’: ’20012375'，'姓名’:’袁萍’，’性别:’女’，’成绩’: ’66’ }
并按照如下格式输出字典元素
'''
#已知两个列表定义如下，分别是学生信息列表和学生信息表头列表：
head=['学号','姓名','性别','成绩']
stuInfo=[
['20012132', '于华美', '女', '90'],
['20012133', '井瑶函', '女', '96'],
['20012141', '刘美玲', '女', '72'],
['20012179', '阳运飚', '男', '88'],
['20012184', '王乳宁', '女', '52'],
['20012186', '艾浩枫', '男', '66'],
['20012248', '王佳铭', '男', '71'],
['20012260', '孟祥竹', '男', '96'],
['20012270', '高艺嘉', '女', '83'],
['20012282', '白益豪', '男', '74'],
['20012285', '刘福聪', '男', '60'],
['20012287', '吴明鹏', '男', '92'],
['20012325', '姜建名', '男', '89'],
['20012327', '艾佳馨', '女', '62'],
['20012330', '张小涵', '女', '57'],
['20012351', '何嘉杰', '男', '66'],
['20012353', '宋杭弛', '男', '53'],
['20012356', '苗旺', '男', '61'],
['20012375', '袁萍', '女', '66']
]

print('董亚杰')
def recursion(num):
    d={}
    for i in range(len(head)):
        d[head[i]]=stuInfo[num][i]
    # print(d)
    return d
for num in range(len(stuInfo)):
    result=recursion(num)
    # print(type(result.items()))  #按题目里的是这个输出格式
    print()
    dInfo=result.items()
    for k,v in dInfo:
        print(k,':',v,end=' ') #按图片里的是这个输出格式