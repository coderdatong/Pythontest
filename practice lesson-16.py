import  math,random
#输入一个三位随机数，如果大于随机数分别输出个位十位百位
#如果等于，输出100并提示中奖
#如果小于，则将120个字符输入到文本文件中（规则每一条字符串长度为十二，前四个字母(用ASCII码转数字)后八个数字）
num=input("请输入一个三位数")
num1=random.randrange(100,1000)
a=int(num)//100
b=int(num)%100
c=int(b)//10
d=int(b)%10
def save():
    '定义一个空字符串用于拼接字符'
    #循环前四个随即字母（用Ascii值来随机，再转换为字母）
    str_num=''
    for i in range(4):
        num2=random.randrange(97,123)
        str_s=chr(num2)
        str_num+=str_s
    for i in range(8):
        num3=random.randrange(0,10)
        str_num+=str(num3)
    return str_num
if int(num)>num1:
    print("digit: {}".format(d)+"  tenthdigit: {}".format(c)+"  hundreddigit: {}".format(a)+num1)
if int(num)==num1:
    print(100+"you are rewarded"+num1)
if int(num)<num1:
   #由于120个字符每一行12个可知只需存入10行就可以
   for i in range(10):
        num4= save()
        #with open as 读写文件的解释https://www.cnblogs.com/ymjyqsx/p/6554817.html
        with open('str_num.txt','w')as f:
            f.write(num4)

