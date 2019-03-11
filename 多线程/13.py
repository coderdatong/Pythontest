import threading
import time
semaphone=threading.Semaphore(3)#最多允许三个线程同时使用资源
def func():
    if semaphone.acquire():
        for i in range(5):
            print(threading.current_thread().getName()+'is using semaphone')
        time.sleep(5)
        semaphone.release()
        print(threading.current_thread().getName()+"release semaphone")
for i in range(8):
    t1=threading.Thread(target=func,args=())
    t1.start()
