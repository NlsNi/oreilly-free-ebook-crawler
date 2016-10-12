import requests
from bs4 import BeautifulSoup
import os
import time
import random

browser_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}


def get_url():
    save_path = 'D:/tmp'
    category = ['business', 'data', 'iot', 'programming', 'security', 'web-platform', 'webops-perf']
    category_num = len(category)
    for i in range(0, category_num):
        url = 'http://www.oreilly.com/' + category[i] + '/free/'
        prefix = url + 'files/'
        html = requests.get(url, headers=browser_header).content.decode('UTF-8')
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.find_all('a', {'data-toggle':  'popover'})
        for item in lis:
            name = str(item['href']).split('/')[-1].split('.')[0]
            pdf_file = prefix + name + '.pdf'
            epub_file = prefix + name + '.epub'
            mobi_file = prefix + name + '.mobi'
            if os.path.exists(save_path):
                pass
            else:
                os.mkdir(save_path)
            with open(save_path + '/' + category[i] + ".txt", 'a') as f:
                f.write(name + ": \r\n")
                f.write(pdf_file + "\r\n")
                f.write(epub_file + "\r\n")
                f.write(mobi_file + "\r\n\r\n")
                sec = random.randrange(1, 2)
                time.sleep(sec)


if __name__ == '__main__':
    get_url()
