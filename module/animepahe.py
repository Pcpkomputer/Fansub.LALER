from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *

def animepahe(x):
    tautan=x
    link1=re.compile(r"mp4upload.com\\/embed-(.+).html\"},")
    link2=re.compile(r"1080p\":.*url\":\".*embed-(.*).html\"}}}}")
    grabber=re.compile(r"http.+/anime/.*/(\d+)")
    link=re.findall(grabber, tautan)
    api='https://animepahe.com/api?m=embed&id='+link[0]+'&p=mp4upload'
    req = Request(api, headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req)
    html=BeautifulSoup(url, 'html.parser')
    print(html)
    l1=re.search(link1,str(html))
    l2=re.search(link2,str(html))
    if l1 is None and l2 is None:
        l2=re.search(r"url\":\".+embed-(.+).html\"}",str(html))
        p480=''
        p720='https://mp4upload.com/'+l2.group(1)
        return(p720,p480)
    else:
        p720='https://mp4upload.com/'+l1.group(1)
        p480='https://mp4upload.com/'+l2.group(1)
        return(p720,p480)
