#encoding:utf-8
import csv
'''
csv
'''
# 1.
# with open('测试数据.csv','r') as fp:
# reader是一个迭代器
#     reader = csv.reader(fp)
#     next(reader)
#     for row in reader:
#         site = row[3]
#         statsu = row[6]
#         print({'地址':site,'状态':statsu})



# 2.
with open('测试数据.csv','r') as fp:
    #不会包含标题那行数据
    reader = csv.DictReader(fp)
    for row in reader:
        print({'地址':row['province_name'],'状态':row['status']})