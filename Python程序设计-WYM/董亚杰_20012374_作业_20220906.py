'''
课后作业：以编号【1，59】代表班内59名同学，随机抽取3名幸运同学（方法不限）
'''
#方法一：
import random
print('董亚杰')
from random import randint
def random_choose(len_num, total):
    lucky_student = []
    while len(lucky_student) < len_num:
        student = randint(1, total) # randint(a, b)生成[a, b]之间的随机数
        if student in lucky_student:
            continue
        else:
            lucky_student.append(student)
    print("抽取的幸运同学为："+str(sorted(lucky_student)).strip('[]'))	# 按照顺序输出

if __name__ == '__main__':
    random_choose(3, 59)	# 在59个人中，随机选择3个人
#方法二：
# student=[]
# for  i in range (1,60):
#     student.append(i)
# print('班级共有'+str(student).strip('[]'))
