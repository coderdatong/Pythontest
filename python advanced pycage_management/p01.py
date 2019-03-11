#包含一个学生类，一个say函数，一个打印语句
class Student():
    def __init__(self,name="chris",age=18):
        self.name=name
        self.age=age
    def say(self):
        print("my name is {0}".format(self.name))
def sayHello():
    print("hello welcome to QingDao university")
    #此判断建议建议一直作为程序的入口
if __name__=='__main__': #判断使用者是否为模块，是则执行，不是模块不执行
    print("i am a module")
