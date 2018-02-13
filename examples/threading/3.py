import threading
import time


# 线程执行的第一个任务
def job1():
    print('T1 Start %s' % threading.current_thread())
    for i in range(10):
        time.sleep(0.1)
        print(i)
    print('T1 End %s' % threading.current_thread())


# 线程执行的第二个任务
def job2():
    print('T2 Start %s' % threading.current_thread())
    print('T2 End %s' % threading.current_thread())


def main():
    # 添加第一个线程
    thread1 = threading.Thread(target=job1, name='T1')
    # 添加第二个线程
    thread2 = threading.Thread(target=job2, name='T2')
    # 运行第一个线程
    thread1.start()
    # 运行第二个线程
    thread2.start()
    # 运行完第一个线程后在执行下面的代码
    thread1.join()
    # 运行完第一个线程后在执行下面的代码
    thread2.join()
    print('all done')


if __name__ == '__main__':
    main()
