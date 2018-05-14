from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from re import *
from flask import jsonify,json

def zippyshare_direct(x):
    link=x
    s=requests.Session()
    r=s.get(link, headers={"user-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"})
    pattern=re.search(r"document\.getElementById\('dlbutton'\).href[\s=]+\"([^\"]+)\"\s+\+\s+\((\d+)\s%\s(\d+)\s+\+\s(\d+)\s%\s(\d+)\)[\s\+]+\"([^\"]+)\";", str(r.text))
    satu=re.sub(r"/\w/.*","",str(link))
    dua=pattern.group(1)
    tiga=int(pattern.group(2))%int(pattern.group(3))+int(pattern.group(4))%int(pattern.group(5))
    empat=pattern.group(6)
    hasil=str(satu)+str(dua)+str(tiga)+str(empat)
    return jsonify(direct=hasil)
