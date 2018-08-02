#encoding:utf-8
import requests

# 使用requests添加代理也非常简单，只要在请求的方法中（比如get或者post）传递proxies参数就可以了。示例代码如下：

proxies = {
    'http':'47.96.18.150:8000'
}


url = "http://httpbin.org/get"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

resp = requests.get(url=url,headers=headers,proxies=proxies)
print(resp.text)


