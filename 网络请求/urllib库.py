from urllib import request

# urlopen函数
# resp = request.urlopen('http://www.baidu.com')
'''
url：请求的url。
data：请求的data，如果设置了这个值，那么将变成post请求。
返回值：返回值是一个http.client.HTTPResponse对象，这个对象是一个类文件句柄对象。
有read(size)、readline、readlines以及getcode等方法'''
# print(resp.read())


'''urlretrieve
这个函数可以方便的将网页上的一个文件保存到本地
resp = request.urlretrieve('https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1402891469,859985910&fm=27&gp=0.jpg',
                'urlretrive.png')'''




'''urlencode函数
用浏览器发送请求的时候，如果url中包含了中文或者其他特殊字符，那么浏览器会自动的给我们进行编码。
 而如果使用代码发送请求，那么就必须手动的进行编码，这时候就应该使用urlencode函数来实现
 '''
from urllib import parse
data = {'name':'董豪','age':18,'school':'nyist'}
data = parse.urlencode(data)
print(data)

'''
parse_qs函数：
可以将经过编码后的url参数进行解码。示例代码如下：'''
ps = parse.parse_qs(data)
print(ps)

