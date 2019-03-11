import multiprocessing
from time import ctime,sleep
def consumer(input_q):
    print("Into Consumer",ctime())
    while True:
        #处理项
        item=input_q.get()
        print("pull",item,"off q")
        input_q.task_done()#发出信号通知任务完成
    print("out of consumer",ctime())

def producer(sequence,output_q):
    print("Into producer",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("Out of Procuder",ctime())

if __name__ == '__main__':
    q=multiprocessing.JoinableQueue()
    cons_p=multiprocessing.Process(target=consumer,args=(q,))
    cons_p.daemon=True
    cons_p.start()
    sequence=[1,2,3,4]
    producer(sequence,q)
    q.join()