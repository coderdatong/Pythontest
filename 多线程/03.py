import  time
import _thread as thread
def loop1(in1):
    #ctime 获取当前时间
    print("start loop1:",time.ctime())
    print("i am an argument",in1)
    time.sleep(4)
    print("end loop1:",time.ctime())

def loop2(in1,in2):
    print("start loop2",time.ctime())
    print("i am argument",in1,"and argument",in2)
    time.sleep(2)
    print("end loop2",time.ctime())

def main():
    print("Starting at ",time.ctime())
    thread.start_new_thread(loop1,("chris", ))
    thread.start_new_thread(loop2,("Tony","Tobby"))

    print("ending at",time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)