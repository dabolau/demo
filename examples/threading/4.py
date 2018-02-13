import threading
import time
from queue import Queue


# 线程执行的第一个任务
def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    # 按顺序把运算结果放入队列
    q.put(l)


# 运行多线程
def multithreading():
    # 定义队列
    q = Queue()
    # 定义线程列表
    threads = []
    # 定义结果列表
    results = []
    # 定义数据
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        # 定义线程，target为线程执行任务，args为线程传入执行任务的参数
        t = threading.Thread(target=job, args=(data[i], q))
        # 运行线程
        t.start()
        # 将线程加入到线程列表里
        threads.append(t)
    for thread in threads:
        # 将所有线程执行完后执行下面的代码
        thread.join()
    for r in range(4):
        # 按顺序从队列取出结果并放入结果列表里
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    multithreading()
