#encoding:utf-8


from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')

html = etree.parse('腾讯.html',parser=parser)

# 获取所有tr标签
# tr = html.xpath('//tr')
count = 0
# for i in tr:
#     print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
#     print('---------------------------------------------------------')
#     count+=1
#     print('tr的数量是:',count)

#获取第二个tr标签
'''
tr = html.xpath('//tr[2]')
tr = html.xpath('//tr[2]')[0]
for i in tr:
    print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
    print('---------------------------------------------------------')'''


# 获取class = even的标签
'''classevent = html.xpath('//*[@class="even"]')
for i in classevent:
    print(etree.tostring(i, encoding='utf-8').decode('utf-8'))
    print('---------------------------------------------------------')
    count+=1
    print('class=event的数量是:',count)'''

# 获取所有a标签中的href值
# hrefs = html.xpath('//a/@href')
# for i in hrefs:
#     print('https://hr.tencent.com/'+i)

# 获取所有的职位信息（纯文本）
jobnames = html.xpath('//td[@class="l square"]/a/text()')
types = html.xpath('//tr[@class="even" or @class="odd"]/td[2]/text()')
places = html.xpath('//tr[@class="even" or @class="odd"]/td[4]/text()')
hrefs = html.xpath('//tr[@class="even" or @class="odd"]/td/a/@href')

for i in range(count):
    print('职位名称:',jobnames[i])
    print('职位类型',types[i])
    print('职位地点',places[i])
    print('职位详情页面'+'https://hr.tencent.com/'+hrefs[i])
    print(i)
    print('---------------------------------')

    #当前元素下面获取，用一个.    例如：'.//td'