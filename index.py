#! -*-coding:utf-8 -*-


import urllib
import re
import download


img_dir = 'imgs/'
key = '刀塔'

# 查询内容
content = urllib.quote(key)
# 查询第几页
page = 1
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&gsm=78&ct=&ic=0&lm=-1&width=0&height=0&pn=%d&word=%s' % (page, content)
res = urllib.urlopen(url)
html = res.read()
result = re.findall(r'flip.setData\(\'imgData\',(.*?)\n', html)
img_urls = re.findall(r'\"middleURL\":\"(.*?)\",', result[0])
for img_url in img_urls:
    download.download_img(img_url, img_dir)

