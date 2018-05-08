from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *
from flask import jsonify,json

def query_oploverz(x):
    url_query='https://www.oploverz.in/?s='+x+'&post_type=post'
    #url_query='https://www.oploverz.in/?s=tada-kun&post_type=post'
    grabber=re.compile(r"<div class=\"thumb\">\s<a href=\"(https://www.oploverz.in/[a-zA-Z-\d/]*)\"")
    req = Request(url_query, headers={'User-Agent': 'Mozilla/5.0'})
    reqs = urlopen(req)
    html = BeautifulSoup(reqs, 'html.parser')
    hasil = re.findall(grabber, str(html))
    return jsonify(results = hasil)