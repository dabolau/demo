import multiprocessing as mp
import threading as td
import time


# 工作任务
def job(q):
    res = 0
    for i in range(100000):
        res += i + i**2 + i**3
    q.put(res)


# 多进程运算
def multicore():
    # 创建一个队列
    q = mp.Queue()
    # 创建一个进程
    p1 = mp.Process(target=job, args=(q,))  # 注意（，）必不可少，否则会报错
    p2 = mp.Process(target=job, args=(q,))  # 注意（，）必不可少，否则会报错
    # 运行一个进程
    p1.start()
    p2.start()
    # 阻塞进程，执行完后在执行后面的代码
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)


# 多线程运算
def multithread():
    # 创建一个队列
    q = mp.Queue()
    # 创建一个线程
    t1 = td.Thread(target=job, args=(q,))  # 注意（，）必不可少，否则会报错
    t2 = td.Thread(target=job, args=(q,))  # 注意（，）必不可少，否则会报错
    # 运行一个线程
    t1.start()
    t2.start()
    # 阻塞线程，执行完后在执行后面的代码
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)


# 正常运算
def normal():
    res = 0
    for _ in range(2):
        for i in range(100000):
            res += i + i**2 + i**3
    print('normal:', res)


if __name__ == '__main__':
    st1 = time.time()
    normal()
    et1 = time.time()
    print('normal time:', et1 - st1)
    st2 = time.time()
    multithread()
    et2 = time.time()
    print('multithread time:', et2 - st2)
    st3 = time.time()
    multicore()
    et3 = time.time()
    print('multicore time:', et3 - st3)
