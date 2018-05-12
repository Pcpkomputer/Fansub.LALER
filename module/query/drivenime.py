from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from re import *
from flask import jsonify,json


def drivenime_query(x):
    query="https://drivenime.com/?s="+x
    req = Request(query, headers={"user-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"})
    op=urlopen(req)
    html=BeautifulSoup(op, 'html.parser')
    link=re.findall(r"<h2 class=\"title\">\s+<a href=\"([^\"]+)\" rel",str(html))
    return jsonify(results=link)
