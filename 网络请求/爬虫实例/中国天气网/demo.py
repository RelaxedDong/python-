#encoding:utf-8
import requests
from bs4 import BeautifulSoup

ALL_DATA= []
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}
import html5lib

def parse_page(url):
        response = requests.get(url,headers=headers)
        text = response.content.decode('utf-8')
        soup = BeautifulSoup(text,'html5lib')
        div = soup.find_all('div',class_='conMidtab')[1]
        tables = div.find_all('table')
        for table in tables:
            trs = table.find_all('tr')[2:]
            for index,tr in enumerate(trs):
                if index == 0:
                    tds = tr.find_all('td')
                    td_city = tds[1]
                    city = list(td_city.find('a').stripped_strings)[0]
                    td_high = tds[4]
                    city_high_temp = list(td_high.stripped_strings)[0]
                else:
                    tds = tr.find_all('td')
                    td_city = tds[0]
                    city = list(td_city.stripped_strings)[0]
                    td_high = tds[3]
                    city_high_temp = list(td_high.stripped_strings)[0]
                print({'城市':city,'最高温度':int(city_high_temp)})
                ALL_DATA.append({'城市':city,'最高温度':int(city_high_temp)})




def get_url():
    url_base = 'http://www.weather.com.cn/textFC/{}.shtml'
    url_list = ['gat','hb','db','hd','hz','hn','xb','xn']
    for url in url_list:
        base = url_base.format(url)
        parse_page(base)


from pyecharts import Bar

def main():
    url = 'http://www.weather.com.cn/textFC/xn.shtml'
    parse_page(url)

if __name__ == '__main__':
    get_url()
    def data_sort(data):
        info = data['最高温度']
        return info
    ALL_DATA.sort(key=data_sort)
    print(len(ALL_DATA))

    bar = Bar("中国气温排行榜top榜")
    city_name = []
    temp = []
    for data in ALL_DATA:
        city_name.append(data['城市'])
        temp.append(data['最高温度'])
    bar.add('气温',city_name[452:],temp[452:])
    bar.render(path='bar.html')




