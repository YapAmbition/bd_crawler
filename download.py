#! -*-coding:utf-8 -*-

import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}


def download_img(url, img_dir):
    path = img_dir + str(hash(url)) + '.' + url.split(".")[-1]
    try:
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
        if not os.path.exists(path):
            session = requests.Session()
            r = session.get(url, headers=headers)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
            print("爬取完成")
        else:
            print("文件已存在")
    except Exception as e:
        print("爬取失败:"+str(e))