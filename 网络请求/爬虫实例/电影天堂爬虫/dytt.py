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
    movie ={}
    xxx = de_html.xpath('//span[@style="FONT-SIZE: 12px"]/a/@href')
    print(xxx)
    infos = de_html.xpath('//div[@id="Zoom"]//p[1]/text()')


    for index,info in enumerate(infos):

        if info.startswith("◎年　　代"):
            year = info.replace('◎年　　代',"").strip()
            movie['year'] = year
        elif info.startswith("◎产　　地"):
            place = info.replace('◎产　　地',"").strip()
            movie['place'] = place
        elif info.startswith("◎类　　别"):
            type = info.replace('◎类　　别',"").strip()
            movie['type'] = type
        elif info.startswith("◎语　　言"):
            language = info.replace('◎语　　言', "").strip()
            movie['language'] = language
        elif info.startswith("◎片　　长"):
            long = info.replace('◎片　　长', "").strip()
            movie['long'] = long
        elif info.startswith("◎导　　演"):
            director = info.replace('◎导　　演', "").strip()
            movie['director'] = director
        elif info.startswith("◎主　　演"):
            info = info.replace('◎主　　演', "").strip()
            actors = [info]
            for i in range(index+1,len(infos)):
                actor = infos[i].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎导　　演"):
            description = info.replace('◎导　　演', "").strip()
            movie['description'] = description




    poster =  de_html.xpath('//div[@id="Zoom"]//p[1]//img[1]/@src')
    haibao = de_html.xpath('//div[@id="Zoom"]//p[1]//img[2]/@src')
    print(poster)
    print(haibao)
if __name__ == '__main__':
    get_detail()

