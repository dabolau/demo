import multiprocessing as mp
import threading as td


# 工作任务
def job(a, b):
    print(a + b)


# 展示了线程(threading)和进程(multiprocessing)的方式几乎一样
if __name__ == '__main__':
    # 创建一个线程
    t1 = td.Thread(target=job, args=(1, 2))
    # 运行一个线程
    t1.start()
    # 阻塞线程，执行完后在执行后面的代码
    t1.join()
    # 创建一个进程
    p1 = mp.Process(target=job, args=(1, 2))
    # 运行一个进程
    p1.start()
    # 阻塞进程，执行完后在执行后面的代码
    p1.join()
