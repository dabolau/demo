import asyncio
import time


async def job(t):
    print('start job ', t)
    await asyncio.sleep(t)  # 等待t秒，并会自己寻找其他工作
    print('job ', t, ' takes ', t, ' s')


async def main(loop):
    tasks = [loop.create_task(job(t))for t in range(1, 6)]  # 只创建，不运行
    await asyncio.wait(tasks)  # 执行工作直到所有工作完成


t1 = time.time()
# 获取事件循环
loop = asyncio.get_event_loop()
# 运行事件循环
loop.run_until_complete(main(loop))
# 关闭事件循环
loop.close()
print('asyncio total time: ', time.time() - t1)
