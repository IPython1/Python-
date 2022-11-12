'''
作业1: .生成包含1000个1~100的随机整数，
并统计每个元素的出现次数【按次数或整数值升序或降序输出统计结果】
要求:至少2种方法(
1-字典+sorted
2-使用collections模块的Counter类)
'''
print('董亚杰')
import random
aL=[random.randint(1,100) for i in range(1000)]
print('生成一个含1000个随机整数(1-100)的列表')
print(aL,len(aL))
# #方法一：遍历所有元素
# # for i in aL:
# #     print(i,':',aL.count(i),'次')
# #方法二：使用字典
# d = dict()
# for v in aL:
#     d[v] = d.get(v ,0) + 1#给每个键赋初值用于计数
# print(d)
# bL=sorted(d.items(),key=lambda x:x[0])
# print(bL,'\n',sum(d.values()))
# print(bL,sum([item[1] for item in d.items()]))
# for k, v in d.items():
#     print(k, v, sep=':')

# 方法三：使用counter类
from collections import Counter
c = Counter(aL)
print(dict(c),type(c))
# for i in aL:
#     print(str(i)+':'+str(c[i])+'次',end=',')

# '''
# 作业2:利用字典输入多名学生姓名、成绩，完成以下2个操作:
# 1-输出对应等级:# 90分以上为‘A’等，89-60分为‘B’等，60分以下为‘℃’等
# 2-计算成绩的最高分、最低分、平均分，并查找所有最高分同学。
# 分析:字典中: key学生姓名: value分数
# '''
Student_dict={
    '杰杰':99,
    '张三':80,
    '李四':70,
    '王五':59
}
for i in Student_dict.keys():
    if  Student_dict[i]>=90:
       print(str(i)+'A等')
    elif   Student_dict[i]>60:
       print(str(i) + 'B等')
    else:
       print(str(i) + 'C等')
score_max=max(Student_dict.values())
print(score_max)
score_min=min(Student_dict.values())
print(score_min)
score_avg=sum(Student_dict.values())/len(Student_dict.values())
print(score_avg)
for key,value in Student_dict.items():
    if (value==score_max):
        print(str(key)+str(value))
# '''
# 作业3:某班有30名学生，利用随机函数在班级内抽取看文艺晚会(5人)、听讲座（12人)同学
# '''
# # import random
# #
# # student = list(range(1,31))
# # print('班里所有人')
# # print(student)
# #
# # wanhui = random.sample(student,5)
# # print('参加晚会的人')
# # print(wanhui)
# #
# # for i in range(5):
# #     student.remove(wanhui[i])
# #
# # jiangzuo = random.sample(student,12)
# # print('参见讲座的人')
# # print(jiangzuo)
# import  random
# Student=random. sample(range(1,31),30)
# print(Student,len(Student))#生成由30个[1,30)随机整数构成的列表 （无重复)
# show_person=random.sample(range(1,len(Student)+1),5)
# print(*show_person,':',len(show_person),'参加文艺晚会')
# def del_show(Student):
#         for x in show_person:
#                 # print(x)
#                 for j in Student[:]:
#                         if j==x:
#                                 Student.remove(j)
#         return Student
# lecture_person=del_show(Student)
# # print(*lecture_person,':',len(lecture_person))
# result=random.sample(range(1,len(lecture_person)+1),12)
# print(*result,':',len(result),'参加讲座')

