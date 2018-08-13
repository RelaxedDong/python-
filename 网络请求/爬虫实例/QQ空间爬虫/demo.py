#encoding:utf-8

import requests
from lxml import etree

url = 'https://user.qzone.qq.com/1417766861/infocenter?via=toolbar&_t_=0.04723397433941612'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'cookie':'1417766861_todaycount=0; 1417766861_totalcount=9257; pgv_pvi=397130752; ptui_loginuin=1417766861; pt2gguin=o1417766861; RK=N4CJSqnBSW; ptcz=f93264b4255d40c3105dc31a4defd66a069bf572c33ad1c99a7dbf7178cf46cd; pgv_pvid=8215791357; QZ_FE_WEBP_SUPPORT=1; qz_screen=1536x864; zzpaneluin=; zzpanelkey=; pgv_si=s1589951488; _qpsvr_localtk=0.9731443564892253; ptisp=cnc; pgv_info=ssid=s3811766276; uin=o1417766861; skey=@ZIgWXzx3k; p_uin=o1417766861; pt4_token=haj9MEGM9Ssx3eGB6CdMJGriHroU-m4FCHutnS2W*HI_; '
             'p_skey=n8TczG--CyAQCt2RY5I-2DPlhASDfE418jJFkk6QuUw_; Loading=Yes; cpu_performance_v8=19',
    'referer':'https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone&specifyurl=http%3A%2F%2Fuser.qzone.qq.com%2F1417766861%2Finfocenter%3Fvia%3Dtoolbar',
    'upgrade-insecure-requests':'1',
    'path':'/1417766861/infocenter?via=toolbar&_t_=0.04723397433941612'
}

resp = requests.get(url=url,headers=headers)
text = resp.text
print(text)