'''
作业1:生成包含1000个1~100的随机整数，并统计每个元素的出现次数
【按次数或整数值升序或降序输出统计结果】
要求:至少2种方法（1-字典+sorted2-使用collections模块的Counter类)
分析：
    传统算法:统计变量=0 统计条件为真 统计变量+1
    100个统计变量
    {key:value}
作业2:利用字典输入多名学生姓名、成绩，完成以下2个操作:
1-输出对应等级:#90分以上为‘A’等，89-60分为‘B’等，60分以下为‘C’等，
2-计算成绩的最高分、最低分、平均分，并查找所有最高分同学。分析:字典中: key学作业3:某班有30名学生，
利用随机函数在班级内抽取看文艺晚会(5人)、听讲座（12人）同学
'''
# 使用字典
# d = dict()
# for v in aL:
#     d[v] = d.get(v ,0) + 1#给每个键赋初值用于计数
# print(d)
# bL=sorted(d.items(),key=lambda x:x[0])
# print(bL,'\n',sum(d.values()))
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