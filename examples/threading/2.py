import threading


# 线程执行的任务
def thread_job():
    print('this is an added thread, number is %s' % threading.current_thread())


def main():
    # 添加一个线程
    added_thread = threading.Thread(target=thread_job)
    # 运行线程
    added_thread.start()

    # print(threading.active_count()) #查看活动的线程数
    # print(threading.enumerate()) #查看正在运行的线程
    # print(threading.current_thread()) #查看当前线程名称


if __name__ == '__main__':
    main()
