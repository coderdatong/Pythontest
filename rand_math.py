import  random
import  math
num=input("请输入一个三位数：")
# 输入函数的是字符类型，不强制转换回报错
if num.isdigit() and 100<=int(num)<=999:
        pass
else:
    print("请按规定输入")


