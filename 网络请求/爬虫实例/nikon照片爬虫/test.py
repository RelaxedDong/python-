from urllib import request


# resp = request.urlretrieve('https://reg.nikon.com.cn/cs_otherspace/show_big_img/280232/448183.jpg','test.jpg')

import time,os
filename = os.path.join(os.getcwd(),'myfile')
print(os.path.join(filename,time.strftime('%Y-%m-%d%H%M%S')+'.jpg'))



