import threading
sum=0
loopsum=1000
lock=threading.Lock()
def addsum():
    global sum,loopsum
    for i in range(1,loopsum):
        #上锁，申请锁
        lock.acquire()
        sum+=1
        #释放锁
        lock.release()
def miusum():
    global  sum,loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum-=sum
        lock.release()
if __name__ == '__main__':
    print("Start ....{0}".format(sum))
    t1=threading.Thread(target=addsum,args=())
    t2=threading.Thread(target=miusum,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done....{0}".format(sum))