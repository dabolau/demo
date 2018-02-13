import multiprocessing as mp


# 工作任务
def job(q):
    res = 0
    for i in range(1000):
        res += i + i**2 + i**3
    q.put(res)


if __name__ == '__main__':
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
    print(res1 + res2)
