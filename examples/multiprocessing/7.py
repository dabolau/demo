import multiprocessing as mp
import time


# 工作任务
def job(v, l, num):
    # 锁住整个工作任务
    l.acquire()
    for i in range(10):
        time.sleep(0.1)
        # 共享内存的值每次加等于传进来的值
        v.value += num
        print(v.value)
    # 释放整个工作任务
    l.release()


# 多进程任务
def multicore():
    # 创建进程锁
    l = mp.Lock()
    # 创建共享内存
    v = mp.Value('i', 0)
    # 创建P1和P2两个进程，分别执行，分别执行完后才能执行后面的代码
    p1 = mp.Process(target=job, args=(v, l, 1))
    p2 = mp.Process(target=job, args=(v, l, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
