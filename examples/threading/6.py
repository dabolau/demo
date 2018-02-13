import threading


def job1():
    # 定义全局变量A和lock锁
    global A, lock
    lock.acquire()  # 打开线程锁
    for i in range(10):
        A += 1
        print('job1, ', A)
    lock.release()  # 释放线程锁


def job2():
    # 定义全局变量A和lock锁
    global A, lock
    lock.acquire()  # 打开线程锁
    for i in range(10):
        A += 10
        print('job2, ', A)
    lock.release()  # 释放线程锁


if __name__ == '__main__':
    # 定义线程锁
    lock = threading.Lock()
    # 定义全局变量
    A = 0
    # 线程一
    t1 = threading.Thread(target=job1)
    # 线程二
    t2 = threading.Thread(target=job2)
    # 运行线程一
    t1.start()
    # 运行线程二
    t2.start()
    # 运行完线程一在执行后面的代码
    t1.join()
    # 运行完线程二在执行后面的代码
    t2.join()
