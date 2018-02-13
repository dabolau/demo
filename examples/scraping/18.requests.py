import requests
import time


url = 'https://www.baidu.com/'


def normal():
    for i in range(1, 6):
        r = requests.get(url)
        u = r.url
        print(u)


if __name__ == '__main__':
    t1 = time.time()
    normal()
    print('normal total time: ', time.time() - t1)
