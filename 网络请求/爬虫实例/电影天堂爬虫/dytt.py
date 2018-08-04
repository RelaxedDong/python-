#encoding:utf-8

import requests
from lxml import etree
from pymongo import MongoClient
import time

conn = MongoClient(host='localhost',port=27017)
db = conn.dytt_spider

collections = db.dytt






headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}


def get_detaul_url():
    movies = []
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for index in range(1,7):
        detail_url = url.format(index)
        response = requests.get(detail_url, headers=headers)
        text = response.text
        html = etree.HTML(text)
        hrefs = html.xpath('//b/a/@href')
        for href in hrefs:
            href = 'http://www.dytt8.net/' + href
            movie = get_detail(href)
            print(movie)
            movies.append(movie)
    for i in movies:
        collections.insert(i)



# detail_url = 'http://www.dytt8.net/html/gndy/dyzz/20180731/57193.html'
#

def get_detail(detail_url):
    de_response = requests.get(detail_url,headers=headers)
    de_text = de_response.content.decode('gbk')
    de_html = etree.HTML(de_text)
    movie ={}
    infos = de_html.xpath('//div[@id="Zoom"]//p[1]/text()')
    download_url = de_html.xpath('//td//a[1]/text()')
    poster =  de_html.xpath('//div[@id="Zoom"]//p[1]//img[1]/@src')
    haibao = de_html.xpath('//div[@id="Zoom"]//p[1]//img[2]/@src')
    title = de_html.xpath('//font[@color="#07519a"]//text()')[0]
    movie['title']=title
    movie['poster']=poster
    movie['haibao']=haibao
    movie['download_url'] = download_url
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
    return movie



if __name__ == '__main__':
    get_detaul_url()

