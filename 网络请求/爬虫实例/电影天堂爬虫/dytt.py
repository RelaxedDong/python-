#encoding:utf-8

import requests
from lxml import etree

url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}

response = requests.get(url,headers=headers)
text = response.content.decode('gbk')
html = etree.HTML(text)
#详情页面获取
# hrefs = html.xpath('//b/a/@href')
# for href in hrefs:
#     print('http://www.dytt8.net/'+href)


detail_url = 'http://www.dytt8.net/html/gndy/dyzz/20180731/57193.html'
def get_detail():
    de_response = requests.get(detail_url,headers=headers)
    de_text = de_response.content.decode('gbk')
    de_html = etree.HTML(de_text)
    title = de_html.xpath('//div[@id="Zoom"]//p[1]/text()')
    for i in title:
        print(i)
    poster =  de_html.xpath('//div[@id="Zoom"]//p[1]//img[1]/@src')
    haibao = de_html.xpath('//div[@id="Zoom"]//p[1]//img[2]/@src')
    print(poster)
    print(haibao)
if __name__ == '__main__':
    get_detail()

