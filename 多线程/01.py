'''
利用time函数，生成两个函数
顺序调用
计算
'''
import  time
def loop1():
    #ctime 获取当前时间
    print("start loop1:",time.ctime())
    time.sleep(4)
    print("end loop1:",time.ctime())

def loop2():
    print("start loop2",time.ctime())
    time.sleep(2)
    print("end loop2",time.ctime())

def main():
    print("Starting at ",time.ctime())
    loop1()
    loop2()
    print("ending at",time.ctime())
if __name__ == '__main__':
    main()