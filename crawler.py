#! -*-coding:utf-8 -*-

import urllib
import re
import download

# 百度默认的
page_size = 20

def start_crawler(img_dir, key, page):
    content = urllib.quote(key)
    pn = 1 if page <= 0 else (page - 1) * 20 + 1
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&gsm=78&ct=&ic=0&lm=-1&width=0&height=0&pn=%d&word=%s' % (pn, content)
    res = urllib.urlopen(url)
    html = res.read()
    result = re.findall(r'flip.setData\(\'imgData\',(.*?)\n', html)
    img_urls = re.findall(r'\"middleURL\":\"(.*?)\",', result[0])
    for img_url in img_urls:
        download.download_img(img_url, img_dir)