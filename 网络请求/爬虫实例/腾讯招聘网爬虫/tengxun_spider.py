#encoding:utf-8


import requests
from lxml import etree
#
# base_utl = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=0'
#
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}



def get_detaul_url():
    url ='https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start={}#a'
    jobs=[]
    for x in range(0,1):

        detail_url = url.format(x*10)

        response = requests.get(url=detail_url, headers=headers)
        text = response.text
        html = etree.HTML(text)
        all_hrefs = html.xpath('//td[@class="l square"]/a/@href')
        for url in all_hrefs:
            hrefs = 'https://hr.tencent.com/' + url
            print(hrefs)
            job = parse_detail(hrefs)
            jobs.append(job)
            print(jobs)


def parse_detail(url):
    response = requests.get(url=url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    post = {}

    title = html.xpath('//td[@id="sharetitle"]/text()')[0]
    position = html.xpath('//tr[@class="c bottomline"]/td/text()')
    duty = html.xpath('//tr[@class="c"][1]//ul/li/text()')
    required = html.xpath('//tr[@class="c"][2]//ul/li/text()')
    post['title']=title
    post['position']=position
    post['duty']=duty
    post['required']=required
    return post

if __name__ == '__main__':
    get_detaul_url()

