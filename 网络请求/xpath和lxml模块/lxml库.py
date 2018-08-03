#encoding:utf-8

from lxml import etree

text = '''
<link rel="apple-touch-icon" href="http://a.xnimg.cn/wap/apple_icon_.png" />
<link rel="stylesheet" type="text/css" href="http://s.xnimg.cn/a86614/nx/core/base.css">
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">上海item</a></li>
         <li class="item-0"><a href="link5.html">重庆</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>'''
result = etree.HTML(text)
# print(result)
# <Element html at 0x3568a80>


# print(etree.tostring(result,encoding='utf-8').decode('utf-8'))

def parse_file():
    htmlelement = etree.parse('hello.html')
    print(etree.tostring(htmlelement,encoding='utf-8').decode('utf-8'))

#解析器改成htmlparse
#
def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlelement = etree.parse('lagou.html',parser=parser)
    print(etree.tostring(htmlelement,encoding='utf-8').decode('utf-8'))

'''除了直接使用字符串进行解析，lxml还支持从文件中读取内容    然后利用etree.parse()方法来读取文件'''
if __name__ == '__main__':
    parse_lagou_file()