#encoding:utf-8
import requests
import re
import time
from urllib import request
import os,time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Cookie':'s_cc=true; REGNIKON=e1qrfiitmt72ih3q9ct3aqoejv; CakeCookie[rTyG6mSDDn5P6TPZrTyG6mSDDn5P6TPZ]=Q2FrZQ%3D%3D.1NraAqug2%2FOfDCQor8JrLCJBEAMZAzRMPtBXI6fx8TKF7AJ%2BE%2FUcQ0UTmNExL4W1; CakeCookie[59jP7HuXmvwjwySdwvWWajm5KwGUtQW]=Q2FrZQ%3D%3D.jI6MAvyh0PWeDXgo%2FpI9KXFDEVZOUDofbNkOfaT2%2FzY%3D; s_sq=%5B%5BB%5D%5D; s_nr=1534835372816'
}
filename = os.path.join(os.getcwd(),'myfile')



def get_high_img_url(url):
    response = requests.get(url,headers=headers)
    html = response.text
    imgs = re.findall(r'<div\sclass="g_l_b">.*?<a\shref=(.*?)">',html,re.S)
    for img in imgs:
        img = img.split("\"")[1]
        oldimg = 'https://reg.nikon.com.cn' + img
        highimg = oldimg.replace('photo','show_big_img')
        get_img(highimg)



def get_img(url):
    response = requests.get(url,headers=headers)
    html = response.text
    ret = html.split('"')
    my_img = 'https://reg.nikon.com.cn'+ret[-2]
    resp = request.urlretrieve(my_img,os.path.join(filename,time.strftime('%Y-%m-%d%H%M%S')+'.jpg'))


def main():
    url = 'https://reg.nikon.com.cn/cs_gallery/recent_upload/p?show=20&direction=desc&page={}'
    for i in range(1,9):
        url = url.format(i)
        response = requests.get(url,headers=headers)
        html = response.text
        detail_urls = re.findall(r'<div\sclass="p_l_b">.*?<a\shref=(.*?)">',html,re.S)
        for detail_url in detail_urls:
            detail_url = detail_url.split("\"")[1]
            get_high_img_url('https://reg.nikon.com.cn'+detail_url)
            time.sleep(1)
        time.sleep(1)




    # imgs = re.findall(r'<div\sclass="p_l_b">.*?<a.*?>.*?<img\ssrc="(.*?)"',html,re.S)
    # for img in imgs:
    #     print('https://reg.nikon.com.cn'+img)





if __name__ == '__main__':
    main()