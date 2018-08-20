#encoding:utf-8
import requests,re

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    text = response.text
    all_poem = []
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>+',text,re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    contents = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    poems = []
    for content in contents:
        ret = re.sub('<.*?>',"",content)
        poems.append(ret.strip())
    for value in zip(titles,dynasties,authors,poems):
        title,dynasty,author,content = value
        po = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        all_poem.append(po)
    print(all_poem)
def main():
    url = 'https://www.gushiwen.org/default_3.aspx'
    parse_page(url)

if __name__ == '__main__':
    main()