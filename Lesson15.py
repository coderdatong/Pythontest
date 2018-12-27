import math
# ceil向上取整
'''
print(math.ceil(5.1))
#floor() 向下取整
print(math.floor(4.2))
import  keyword
# 系统关键字，不可用来当作变量名
print(keyword.kwlist)
#round四舍五入操作
print(round(5.02))
#开平方 sqrt,返回浮点数
print(math.sqrt(25))
#pow 计算一个数的几次方，有两个参数，第一个是底数第二个是指数
print(math.pow(3,4))
#fabs()对一个数值获取他的绝对值
print(math.fabs(-19))
#abs()获取绝对值，是python内置函数
print(abs(-3))
#fsum() 求和 返回浮点数
#sum()python 内置求和 返回整数
print(math.fsum([1,3,4,5]))
print(sum([1,3,4,5]))
#math.modf() 将一个浮点数拆分为整数部分和小数部分组成的元组
print(math.modf(4.5))
#copysign()将第二个数的符号付给第一个
print(math.copysign(2,-3))
#打印自然对数e和派的值
print(math.e)
print(math.pi)
#random() 获取0到1之间的随机小数，包括零不包括一'''
import random
'''
for i in range(10):
    print(random.random())
    #随机指定开始和结束之间的值,可以指定之间的值
    print(random.randint(1,9))
#choice 随机获取列表中的值
print(random.choice([1,2,3,4,5,5]))
#shuffle()随机打乱序列 返回值是none
list=[1,2,3,4,5]
print(list)
print(random.shuffle(list))
print(list)
#uniform() 随机获取指定范围内的值（包括小数）
print(random.uniform(1,9))

'''