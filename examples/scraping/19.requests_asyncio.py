import aiohttp
import asyncio
import time

url = 'https://www.baidu.com/'


async def job(session):
    response = await session.get(url)
    return str(response.url)


async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for i in range(1, 6)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]
        print(all_results)


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print('asyncio total time: ', time.time() - t1)
