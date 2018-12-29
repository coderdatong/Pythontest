import  random
import  math
str_num=''
for i in range(4):
    num2 = random.randrange(97, 123)
    str_s = chr(num2)
    str_num += str_s
for i in range(8):
    num3 = random.randrange(0, 9)
    str_num += str(num3)
print(str_num)


