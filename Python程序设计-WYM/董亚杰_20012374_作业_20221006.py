'''
模拟十名观众随机选取任意数目电影(共10部电影，至少为3部电影打分）为其打分(1-5分)运行结果格式为:观众:{电影1:分数，电影2:分数，……}

'''
# from random import randrange
# audience = {'电影' + str(randrange(1, 11)): '分数' + str(randrange(1, 6)) for i in range(4,11)}
# print('观众：'+str(audience))
print()
import random as r
movie = [i for i in range(1,11)] #列表表达式
print(movie)
d={'观众'+str(k):{'电影'+str(x):r.randint(1,5) for x in r.sample(movie,k=r.randint(3,10))} for k in range(1,11)}
for a in d.keys():
    print(a,d[a])
