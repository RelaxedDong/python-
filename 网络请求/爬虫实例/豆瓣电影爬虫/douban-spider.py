#encoding:utf-8
import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com'
}
url = 'https://movie.douban.com/cinema/nowplaying/chongqing/'
resp = requests.get(url=url,headers=headers)
# resp.content是原生数据，没有经过编码,是tytes类型
# resp.text是str类型
text = resp.text


#对数据进行提取解析

parser = etree.HTMLPullParser(encoding='utf-8')
html = etree.HTML(text=text,parser=parser)
ul = html.xpath('//ul[@class="lists"]')[0]
lis = ul.xpath('./li')
movie = []
for li in lis:
    titles = li.xpath('./@data-title')[0]
    scores = li.xpath('./@data-score')[0]
    years = li.xpath('./@data-release')[0]
    times = li.xpath('./@data-duration')[0]
    places = li.xpath('./@data-region')[0]
    directors = li.xpath('./@data-director')[0]
    actors = li.xpath('./@data-actors')[0]
    posters = li.xpath('.//li[@class="poster"]//img/@src')[0]
    movies = {
        'poster':posters,
        'title':titles,
        'score':scores,
        'year':years,
        'time':titles,
        'place':places,
        'director':directors,
        'actor':actors,
    }
    movie.append(movies)
print(movie)


