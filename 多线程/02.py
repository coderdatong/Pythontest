import  time
import _thread as thread
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
    #start_newthread 启动一个多线程，（）表示函数所需要的元组
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("ending at",time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)#主线程不终止