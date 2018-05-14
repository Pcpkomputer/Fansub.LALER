from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from re import *
from flask import jsonify,json

def googledrive_direct(x):
    link=x
    link=link.replace(r"open?",r"uc?")
    auth=re.search(r"&export=download",str(link))
    if auth:
        link=link
    else:
        link=link+'&export=download'
    return jsonify(direct=link)
    #togel=re.search(r"confirm=([^&]+)&id=(.*)",str(hasil))
    #confirm=togel.group(1)
    #idgd=togel.group(2)
    #parameter = {'export': 'download', 'confirm': confirm, 'id':idgd}
    #req=s.get('https://drive.google.com/uc', params=parameter)
    #print(req.text)
