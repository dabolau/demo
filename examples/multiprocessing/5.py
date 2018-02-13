import multiprocessing as mp


# 工作任务
def job(x):
    return x * x


# 多进程任务，进程池会自动全部利用（CPU）的所有核心或进程
def multicore():
    # 创建进程池
    pool = mp.Pool(processes=1)  # 用(PROCESSES)来设置具体要使用多少个核心
    # 传0-9的数字进工作任务中运算，（POOL）可以使用（RETURN）返回结果
    res = pool.map(job, range(100000))
    # 打印返回结果
    print(res)
    # 用（apply_async）只能使用一个值
    res = pool.apply_async(job, (1000,))
    print(res.get())
    # 迭代的方式用（apply_async）来输出多个内容
    multi_res = [pool.apply_async(job, (i,))for i in range(1000)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()
