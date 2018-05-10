from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *

def anitoki(x):
        ####
        googledrive=re.compile(r"href=\"([\w://\d\s.?=-]+)\"\s+rel=\"noopener\"\s+target=\"_blank\">Drive")
        datafilehost=re.compile(r"href=\"([\w://\d\s.?=-]+)\"\s+rel=\"noopener\"\s+target=\"_blank\">Datafilehost")
        zippyshare=re.compile(r"href=\"([\w://\d\s.?=-]+)\"\s+rel=\"noopener\"\s+target=\"_blank\">Zippyshare")
        uppit=re.compile(r"href=\"([\w://\d\s.?=-]+)\"\s+rel=\"noopener\"\s+target=\"_blank\">Uppit")
        mirror=re.compile(r"href=\"([\w://\d\s.?=-]+)\"\s+rel=\"noopener\"\s+target=\"_blank\">Mirror")
        ####
        tautan=x
        req = Request(tautan, headers={'User-Agent': 'Mozilla/5.0'})
        link=urlopen(req)
        html=BeautifulSoup(link,'html.parser')
        gd=re.findall(googledrive,str(html))
        dt=re.findall(datafilehost,str(html))
        zippy=re.findall(zippyshare,str(html))
        upt=re.findall(uppit,str(html))
        mirror=re.findall(mirror,str(html))
        ####
        nama=['360p','480p','720p','480p[h265]','720p[h265]']
        ####
        return(nama,gd,dt,zippy,upt,mirror)
