#encoding:utf-8

from bs4 import BeautifulSoup

html = '''
<table class="tablelist" cellspacing="0" cellpadding="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43108&amp;keywords=&amp;tid=87&amp;lid=0">SNG17-QQ轻游戏平台web前端开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>重庆</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43094&amp;keywords=&amp;tid=87&amp;lid=0">25663-医疗云高级后台研发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>哟要类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43083&amp;keywords=&amp;tid=87&amp;lid=0">TEG02-后台开发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>2类</td>
					<td>2</td>
					<td>重庆</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43074&amp;keywords=&amp;tid=87&amp;lid=0">18428-财付通银行交易开发工程师（深圳）</a></td>
					<td>3类</td>
					<td>2</td>
					<td>万州</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43057&amp;keywords=&amp;tid=87&amp;lid=0">TEG06-高级应用开发工程师(golang&nbsp;或&nbsp;nodejs)(深圳)</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43049&amp;keywords=&amp;tid=87&amp;lid=0">SNG11-高级Web前端开发工程师（深圳）</a></td>
					<td>4类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43051&amp;keywords=&amp;tid=87&amp;lid=0">TEG13-接入平台研发总监（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43047&amp;keywords=&amp;tid=87&amp;lid=0">25924-iOS研发工程师(深圳)</a></td>
					<td>9类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43039&amp;keywords=&amp;tid=87&amp;lid=0">WXG10-113 企业微信后台开发工程师（成都）</a></td>
					<td>5类</td>
					<td>1</td>
					<td>成都</td>
					<td>2018-08-03</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43034&amp;keywords=&amp;tid=87&amp;lid=0">MIG09-Android客户端开发（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>广州</td>
					<td>2018-08-03</td>
					
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1468</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1460#a">147</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    			
		    		</td>
		    	</tr>
		    </tbody></table>
'''

bs = BeautifulSoup(html,'lxml')

#获取所有tr标签
# trs = bs.find_all('tr')


#获取第二个tr标签
tr2 = bs.find_all('tr',limit=2)[1]

#获取所有tr  class='even'的标签

# even1 = bs.find_all('tr',class_='even')
# for i in even1:
#     print(i)
#     print('----------------------')

#或者

even2 = bs.find_all('tr',attrs={'class':'even'})
# for i in even2:
#     print(i)
#     print('----------------------')


#a id=test class=test的标签
a1 = bs.find_all('a',attrs={'id':'test','class':'test'})
a2 = bs.find_all('tr',class_='test',id='test')

#a href的值

# aList = bs.find_all('a')
# print(aList[1])

# for a in aList:
#     print(a['href'])
#     print('-----------')

# for a in aList:
#     print(a.attrs['href'])


#获取所有职位信息,纯文本

trs = bs.find_all('tr')[1:-1]
for tr in trs:
    tds = tr.find_all('td')
    title = tds[0].text
    print(title)

#，然后用 get_text() 方法来获取它的内容。

