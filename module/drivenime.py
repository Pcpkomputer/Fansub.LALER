from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from re import *
from module.bypasser.bagilagi import bagilagi_bypass

def drivenime(x):
    url_awal=x
    req = Request(url_awal, headers={"user-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"})
    res = urlopen(req)
    html = BeautifulSoup(res, "html.parser")
    bagilagi=re.findall(r"href=\"(http(s|)://bagilagi.com/[^\"]+)\" rel=\"nofollow\">[^p]+p]",str(html))
    #indexbl=len(bagilagi)-2
    reso=re.findall(r"nofollow\">[^<]+[^p]/a>([^<]+)<p>",str(html))
    gd=[]
    resoz=[]
    for x in range(3):
        a=str(reso[x]).replace(r"\xa0",r"")
        a=re.sub(r"\s","",a)
        resoz.append(a)
        
    for x in range(3):
        a=str(bagilagi[x]).replace(r"('","")
        a=a.replace(r"', '')","")
        kodetogel=re.search(r"\?id=(.*)",str(a))
        html=bagilagi_bypass(kodetogel.group(1))
        drive=re.search(r"changeLink\(\){var a=\'([^']+)\';window",str(html))
        gd.append(drive.group(1))
    return(resoz,gd)
        
    #if indexbl>0:
    #    for x in range(2,len(bagilagi)):
    #        a=str(bagilagi[x]).replace(r"('","")
    #        a=a.replace(r"', '')","")
    #        print(a)
    #else:
    #    pass
    
