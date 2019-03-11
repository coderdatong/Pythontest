import  threading
from time import sleep,ctime

class ThreadFunc:
    def __init__(self,name):
        self.name=name
    def loop(self,nloop,nsec):
        #nloop:loop函数的名称
        #nsec 系统休眠时间
        print("start loop",nloop,"at",ctime())
        sleep(nsec)
        print("end loop",nloop,"at",ctime())
def main():
    print("Starting at",ctime())
    t=ThreadFunc("loop")
    #t1 t2 意思相同，t2的写法更工业化
    t1=threading.Thread(target=t.loop,args=("loop1",4))
    t2=threading.Thread(target=ThreadFunc("loop").loop,args=("loop2",2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All done",ctime())
if __name__ == '__main__':
    main()