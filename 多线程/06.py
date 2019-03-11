import  time
import  threading as thread
def loop1(in1):
    #ctime 获取当前时间
    print("start loop1:",time.ctime())
    print("i am an argument", in1)
    time.sleep(6)

    print("end loop1:",time.ctime())

def loop2(in1,in2):
    print("start loop2",time.ctime())
    print("i am argument", in1, "and argument", in2)
    time.sleep(1)
    print("end loop2",time.ctime())
def loop3():
    print("Start loop3",time.ctime())
    time.sleep(5)
    print("end loop3",time.ctime())
def main():
    print("Starting at ",time.ctime())
    t1=thread.Thread(target=loop1,args=("guodatong",))
    t1.setName("THR_1")
    t1.start()
    t2=thread.Thread(target=loop2,args=("chris","Tony"))
    t2.setName("THR_2")
    t2.start()
    t3=thread.Thread(target=loop3,args=())
    t3.setName("THR_3")
    t3.start()
    time.sleep(3)
    for thr in thread.enumerate():#得到正在运行的子线程
        print("正在运行的线程名字是：{0}".format(thr.getName()))
    print("正在运行的子线程数量为{0}".format(thread.activeCount()))
    print("ending at",time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)