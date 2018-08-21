#encoding:utf-8
import csv

# headers = ['姓名','年龄','学校','地址']
#
# datas = [
#     ('董豪',20,'nyist','南阳'),
#     {'谭雅',20,'cqist','重庆'},
#     ['谭雅',20,'cqist','重庆'],
#     ['谭雅',20,'cqist','重庆'],
#     ['谭雅',21,'cqist','重庆'],
#
# ]
# with open('my.csv','w',encoding='utf-8',newline="") as fp:
#     mywriter = csv.writer(fp)
#     mywriter.writerow(headers)
#     mywriter.writerows(datas)





headers = ['name','age','classroom']
values = [
    {"name":'wenn',"age":20,"classroom":'222'},
    {"name":'abc',"age":30,"classroom":'333'}
]
with open('test.csv','w',newline='') as fp:
    writer = csv.DictWriter(fp,headers)
    writer = csv.writeheader()
    writer.writerow({'name':'zhiliao',"age":18,"classroom":'111'})
    writer.writerows(values)
