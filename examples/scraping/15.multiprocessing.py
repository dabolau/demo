from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import multiprocessing as mp
import time
import re

base_url = 'https://morvanzhou.github.io/'

if base_url != 'https://127.0.0.1:4000/':
    restricted = True
else:
    restricted = False


def crawl(url):
    response = urlopen(url)
    time.sleep(0.1)
    return response.read().decode()


def parse(html):
    soup = BeautifulSoup(html, features='lxml')
    urls = soup.find_all('a', attrs={'href': re.compile('^/.+?/+$')})
    title = soup.find('h1').get_text().strip()
    for url in urls:
        page_urls = set([urljoin(base_url, url['href'])])
        print(page_urls)
    url = soup.find('meta', attrs={'property': 'og:url'})['content']
    return title, page_urls, url


unseen = set([base_url, ])
seen = set()
pool = mp.Pool(4)
count, t1 = 1, time.time()

while len(unseen) != 0:
    if restricted and len(seen) >= 10:
        break

    print('\nDistributed Crawling...')
    # 单进程方法
    # htmls = [crawl(url) for url in unseen]
    # 多进程方法
    crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jobs]

    print('\nDistributed Parsing...')
    # 单进程方法
    # results = [parse(html) for html in htmls]
    # 多进程方法
    parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]

    print('\nAnalysing...')
    seen.update(unseen)
    unseen.clear()

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)

print('Total time: %.1f s' % (time.time() - t1, ))
