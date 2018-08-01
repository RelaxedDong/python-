from urllib import request,parse

'''urlsplit'''
# 有时候拿到一个url，想要对这个url中的各个组成部分进行分割，那么这时候就可以使用urlparse或者是urlsplit来进行分割。示例代码如下：
url = 'https://www.baidu.com/baidu;hello?wd=%E5%9B%BE%E7%89%87&tn=monline_4_dg&ie=utf-8#a'
# 运行结果：SplitResult(scheme='https', netloc='www.baidu.com', path='/baidu', query='wd=%E5%9B%BE%E7%89%87&tn=monline_4_dg&ie=utf-8', fragment='a')
result = parse.urlsplit(url)
print(result)
# 取到各部分内容
# print(result)
# print('scheme:',result.scheme)
# print('netloc:',result.netloc)
# print('path:',result.path)
# print('query:',result.query)

'''urlparse'''

result1 = parse.urlparse(url)
print(result1)


# 打印结果：
'''
SplitResult(scheme='https', netloc='www.baidu.com', path='/baidu;hello', query='wd=%E5%9B%BE%E7%89%87&tn=monline_4_dg&ie=utf-8', fragment='a')
ParseResult(scheme='https', netloc='www.baidu.com', path='/baidu', params='hello', query='wd=%E5%9B%BE%E7%89%87&tn=monline_4_dg&ie=utf-8', fragment='a')'''

'''
urlparse和urlsplit基本上是一模一样的。唯一不一样的地方是，urlparse里面多了一个params属性，而urlsplit没有这个params属性'''





