import time


def job(t):
    print('start job: ', t)
    time.sleep(t)  # 等待t秒
    print('job ', t, ' takes ', t, ' s')


def main():
    m = [job(t)for t in range(1, 6)]
    print(m)


t1 = time.time()
main()
print('no asyncio total time: ', time.time() - t1)
