from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from re import *
from flask import jsonify,json

def elsfile_direct(x):
    l=x
    reqid=re.findall(r"elsfile.org/(.*)",str(l))[0]
    headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '100',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'elsfile.org',
    'Origin': 'http://elsfile.org',
    'Referer': 'http://elsfile.org/'+reqid,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
    
    dta={
    'op': 'download2',
    'id': reqid,
    'rand':'' ,
    'referer': 'q',
    'method_free': 'Free Download',
    'method_premium':'',
    'down_script':'1',
        }
    
    ses=requests.Session()
    tautan=ses.post(l,data=dta,headers=headers).url
    return jsonify(direct=tautan)
    
    
