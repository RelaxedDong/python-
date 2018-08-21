#encoding:utf-8
import requests,re,time

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}


def parse_page(url):
    response = requests.get(url)
    text = response.text
    contents = re.findall(r'<div\sclass="content">.*?<span>(.*?)</span>',text,re.S)
    imgs = re.findall(r'<div\sclass="thumb">.*?<a.*?>.*?<img.*?src="(.*?)"',text,re.S)
    print(imgs)
    for img in imgs:
        print('https:'+img)
    # for content in contents:
    #     ret = re.sub(r'<.*?>',"",content)
    #     print(ret)


import time
def main():
    url_base = 'https://www.qiushibaike.com/8hr/page/{}/'
    for index in range(2,3):
        url = url_base.format(index)
        parse_page(url)

if __name__ == '__main__':
    main()